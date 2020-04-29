
from django.conf.urls import include, url
from django.urls import path
import agenda.views

app_name = 'agenda'


urlpatterns = [
    url(r'^list/$',   agenda.views.list, name='list'),  
    url(r'^create/$', agenda.views.create, name='create'),
    url(r'^update/(?P<id>\d+)$', agenda.views.update, name='update'),
    url(r'^view/(?P<id>\d+)$', agenda.views.view, name='detail'),
    url(r'^(?P<id>[0-9]+)/vote/$', agenda.views.vote, name='vote'),

    path('delete/<int:id>', agenda.views.destroy),  
]