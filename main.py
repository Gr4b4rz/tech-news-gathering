from es_connection import ESWrapper


def main():
    es_wrapper = ESWrapper()
    es_conn = es_wrapper.connect_elasticsearch()
    es_wrapper.create_index(es_conn, "processed-data")


if __name__== "__main__":
    main()
