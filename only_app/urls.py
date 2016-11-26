from django.conf.urls import url

from . import views


app_name = 'only_app'
#This sets application namespace to diffretiate urls of different apps.

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),

    #url for
    url(r'^yo1$', views.ansible, name='ansible'),

    #url
    url(r'^term$', views.getTer, name='getTer'),

    #url
    url(r'^terminal$', views.openTer, name='openTer'),
    ]