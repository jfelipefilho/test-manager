
from django.conf.urls import url

from . import views

app_name = 'runs'
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^updated_runs/$', views.updated_runs, name='updated'),
        ]
