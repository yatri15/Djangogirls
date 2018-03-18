from django.contrib import admin
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.test, name="test"),
    url(r'^$', views.test, name="index"),
]
