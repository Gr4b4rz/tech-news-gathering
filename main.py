import requests
from bs4 import BeautifulSoup as Bsoup
from es_connection import ESWrapper


def main():
    url = "https://en.wikipedia.org/wiki/Web_crawler"
    req = requests.get(url)
    assert req.status_code == 200
    # soup_req = Bsoup(req.text, "lxml")

    # print(soup_req.prettify())

    es_wrapper = ESWrapper()
    es = es_wrapper.connect_elasticsearch(port=9200)
    es_wrapper.create_index(es, "raw-crawler-data")
    es_wrapper.create_index(es, "processed-data")


if __name__== "__main__":
    main()
