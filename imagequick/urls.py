from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from imagequick.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',index,name='home'),
    url(r'^images/',include('base.urls',namespace='base')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
