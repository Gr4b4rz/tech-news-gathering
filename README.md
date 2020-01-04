# System that gathers information and news about any innovations in tech world

## Installation

1. Prepare your virtual environment.

    ```console
    pip3 install virtualenv
    python3 -m venv ENV
    source ENV/bin/activate
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

    Start docker-compose from root project folder.

    ```console
    cd tech-news-gathering
    sudo docker-compose up
    ```

3. Using pip install requirements:

    ```console
    pip3 install -r requirements.txt
    ```

## Usage

```console
python3 main.py
```
