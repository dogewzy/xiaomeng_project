from . import views
from django.conf.urls import url


app_name = 'registration'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/$', views.search, name='search'),
    url(r'^display/$', views.display, name='display'),
]


