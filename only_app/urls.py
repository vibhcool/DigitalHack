from django.conf.urls import url

from . import views


app_name = 'only_app'
#This sets application namespace to diffretiate urls of different apps.

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),

    #url for home-page:
    url(r'^$', views.ansible, name='ansible'),

    ]