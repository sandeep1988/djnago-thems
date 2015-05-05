from django.conf.urls import patterns, url
from products.models import Product
from products import views

urlpatterns = patterns('',
  url(r'^$', views.product_list, name='product_list'),
  url(r'^new$', views.product_create, name='product_new'),
  url(r'^product_list_data$', views.product_list_data, name='product_list_data'),
  url(r'^product_list_demo$', views.product_list_demo, name='product_list_demo'),
  url(r'^edit/(?P<pk>\d+)$', views.product_update, name='product_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.product_delete, name='product_delete'),
  url(r'^/page/(?P<page>\d+)/$', 'products.views.product_list'),
)