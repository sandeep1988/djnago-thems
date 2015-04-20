from django.conf.urls import patterns, url

from categories import views

urlpatterns = patterns('',
  url(r'^$', views.category_list, name='category_list'),
  url(r'^new$', views.category_create, name='category_new'),
  url(r'^edit/(?P<pk>\d+)$', views.category_update, name='category_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.category_delete, name='category_delete'),
)