from django.conf.urls import url
from . import views

app_name = 'medicine'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
]
