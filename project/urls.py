from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^manager/(?P<adminid>\d+)', views.manager, name='manager'),
    url(r'^employee/(?P<empid>\d+)', views.employee, name='employee'),
)
