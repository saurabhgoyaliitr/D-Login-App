
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
url (r'^polls/' , include('polls.urls' , namespace = "polls")) , 
url(r'^admin/', include(admin.site.urls)),
url ( r'^login/' , include ('login.urls' , namespace = "login" )) , 
 

) + static (settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
