

from django.conf.urls import patterns, include, url

from . import views



urlpatterns = patterns('',
    url(r'^main/$', views.main ),
    url (r'^$', views.login_user),
   url ( r'^register/$' , views.register) , 
   url ( r'^logout/$' , views.logoutu) , 
   url  ( r'^change/$' , views.change) , 

)
 



  

