from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^mail/',views.simple_mailtest,name='simple_mailtest')
]