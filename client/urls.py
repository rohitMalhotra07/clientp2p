from django.conf.urls import patterns, include, url
from clientNode.views import *
from chat.views import *
 
urlpatterns = patterns('',
	url(r'^$',login),
    url(r'^register/$', register),
    url(r'^home',home),
    url(r'^logout',logout_page),
    url(r'^checkvalidusername',checkvalidusername),
    url(r'^chat',chat),
    url(r'^addchat',addchat),

)