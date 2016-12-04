from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patient/$', views.patient, name='patient'),
    url(r'^patient_log/$', views.patient_log, name='patient_log'),
    url(r'^patient_edit/$', views.patient_edit, name='patient_edit'),
    url(r'^patient_search/$', views.patient_search, name='patient_search'),
    url(r'^patient_num/$', views.patient_num, name='patient_num'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
