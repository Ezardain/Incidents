from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<empid>\d+)/$', views.employee, name='employee'),
    url(r'^worker/(?P<empid>\d+)/$', views.worker, name='worker')

)