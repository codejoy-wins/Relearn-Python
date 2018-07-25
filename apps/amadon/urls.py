from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy1', views.buy1),
    url(r'^buy2', views.buy2),
    url(r'^checkout', views.checkout),
    url(r'^clear', views.clear),

    url(r'^', views.odell),
]