from django.conf.urls import patterns, include, url
from .views import IndexView, LogInView

urlpatterns = patterns('',
    url(r'^$' , IndexView.as_view(), name="index"),
    url(r'^log-in/$', LogInView.as_view(), name="login"),
    url(r'^log-out/$', 'apps.home.views.LogOut', name='logout'),
)
