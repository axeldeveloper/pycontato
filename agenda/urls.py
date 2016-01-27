from django.conf.urls import url

from . import views

app_name = 'agenda'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contato_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<contato_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<contato_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^criar/$', views.criar, name='criar'),
    url(r'^edit/(?P<contato_id>\d+)$', views.edit, name='edit')
]