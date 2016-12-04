from django.conf.urls import url
from . import views

app_name = 'price'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^medicine_information/$', views.medicine_information, name='medicine_information'),
    url(r'^main_information/$', views.main_information, name='main_information'),
    url(r'^result/$', views.result, name='result'),
    url(r'^result/$', views.display, name='display'),
]
