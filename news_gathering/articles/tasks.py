from celery import task
from celery.utils.log import get_task_logger
from .parser import parse_article
logger = get_task_logger(__name__)


@task(name="new_article_task")
def parse_article_task(url):
    logger.info("Got article to parse")
    return parse_article(url)