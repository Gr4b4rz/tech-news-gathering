# System that gathers information and news about any innovations in tech world

## Installation

1. Create folder for elastic data.

    ```console
    mkdir esdata
    ```

2. Setup elasticsearch

    As root run:

    ```console
    echo vm.max_map_count=262144 >> /etc/sysctl.conf
    sysctl -p
    ```

    You need to install docker and docker-compose on your machine.
    There are many guides in web how to do it.
    Having installed docker, make sure docker service is running.

    ```console
    sudo service docker start
    ```
3. Build project

    Start docker-compose from root project folder.

    ```console
    cd tech-news-gathering
    sudo docker-compose up
    ```

## Usage
Find elasticsearch cluster on: http://localhost:9200/

Find django app on: http://localhost:8003/articles/

Schedule new site to be scraped
```console
curl -XPOST -d '{"site-url": "ARTICLE-URL"}' localhost:8003/articles/task```

Go to http://localhost:9200/processed-data/_search, to see all scraped articles