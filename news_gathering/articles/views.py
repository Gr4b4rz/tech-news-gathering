from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .tasks import parse_article_task
from django.views.decorators.csrf import csrf_exempt

from .forms import ArticleTask
from newspaper import Article
# Create your views here.


from django.views.generic.edit import FormView

@csrf_exempt
def new_article_task(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        url = body['site-url']
        print(url)
        parse_article_task.delay(url)
        return HttpResponse("Added")
    elif request.method == 'GET':
        return HttpResponse('Hello')


def parse_article(request):

    return HttpResponse("hello world")