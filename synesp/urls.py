from . import views
from django.conf.urls import url

app_name = 'synesp'
urlpatterns = [
    url(r'^criar/$', views.criar, name='criar')
]