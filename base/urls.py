from django.conf.urls import patterns, include, url
from base.views import *

urlpatterns = patterns('',
   
    url(r'^lister$',lister,name='lister'),
    url(r'^search$',find_template,name='find'),
)
