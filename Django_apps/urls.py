from django.conf.urls import patterns, include, url
#from products.views import foo
from django.contrib import admin

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'products.views.product_list', name='product_list'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('categories.urls')),
)
