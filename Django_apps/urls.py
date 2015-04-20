from django.conf.urls import patterns, include, url
#from products.views import foo
from django.contrib import admin

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'products/$', foo),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('categories.urls')),
)
