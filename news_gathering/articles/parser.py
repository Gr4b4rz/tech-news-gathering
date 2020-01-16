from newspaper import Article
from .es_connection import ESWrapper


def parse_article(url):
    a = Article(url)
    a.download()
    a.parse()
    a.nlp()
    es = ESWrapper.connect_elasticsearch(host='es', port=9200)
    es.index(index="processed-data", body={"tags": list(a.tags), "text": a.text, "authors": a.authors, "title": a.title, "keywords": list(a.keywords)})