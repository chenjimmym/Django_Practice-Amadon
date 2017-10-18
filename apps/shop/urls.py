from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_buy', views.process_buy),
    url(r'^checkout', views.checkout),
    url(r'^back', views.back),
]