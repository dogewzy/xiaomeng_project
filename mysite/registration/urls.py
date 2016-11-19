from . import views
from django.conf.urls import url


app_name = 'registration'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^search/$', views.search, name='search'),
]


