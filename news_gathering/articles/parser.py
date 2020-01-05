from newspaper import Article
from .es_connection import ESWrapper


def parse_article(url='https://realpython.com/asynchronous-tasks-with-django-and-celery/#add-the-task'):
    a = Article(url)
    a.download()
    a.parse()
    a.nlp()
    es = ESWrapper.connect_elasticsearch()
    es.index(index="processed-data", body={"tags": list(a.tags), "text": a.text, "authors": a.authors, "title": a.title, "keywords": list(a.keywords)})