from django.conf.urls import url
from . import views

app_name = 'diagnose'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^diagnose/$', views.index, name='index'),
]
