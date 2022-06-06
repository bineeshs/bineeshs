
from django.urls import path

from .import views

app_name='searchapp'
urlpatterns = [
    path(r'^(?P<SearchResult)/$', views.SearchResult,name='SearchResult'),
]