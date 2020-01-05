from elasticsearch import Elasticsearch


class ESWrapper:
    """
    Elasticsearch wrapper
    """
    @staticmethod
    def connect_elasticsearch(host='es1', port=9200):
        """
        Establish connection with Elasticsearch database.
        """
        es = None
        es = Elasticsearch([{'host': host, 'port': port}])
        if es.ping():
            print('Connected')
        else:
            print('Cannot connect')
        return es

    @staticmethod
    def insert_document(es_object, index_name, body):
        return es_object.index(index=index_name, body=body)

    @staticmethod
    def create_index(es_object, index_name):
        """
        Create index if it does not exists.
        """
        created = False
        # index settings
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "members": {
                    "dynamic": "strict",
                    "properties": {
                        "title": {
                            "type": "text"
                        }
                    }
                }
            }
        }
        try:
            if not es_object.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                es_object.indices.create(index=index_name, ignore=400, body=settings)
                print('Created Index')
            created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created

