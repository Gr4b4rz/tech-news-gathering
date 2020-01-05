from django.urls import path

from . import views

urlpatterns = [
    path('', views.parse_article, name='parse-article'),
    path('task', views.new_article_task, name='new-task')
]