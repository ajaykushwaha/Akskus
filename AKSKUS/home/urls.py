from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.home,name="a_she"),


]