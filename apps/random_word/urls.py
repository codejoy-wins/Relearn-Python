from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new),
    url(r'^create', views.create),
    url(r'^reset$', views.reset),
    url(r'^generate$', views.generate),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<word>\w+)$', views.show_word),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/destroy$', views.destroy),

    url(r'^', views.odell),
]