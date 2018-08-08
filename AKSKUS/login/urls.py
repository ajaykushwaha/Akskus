from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'login'
urlpatterns = [
    url(r'^login/$',views.login_in,name='login'),
    url(r'$', TemplateView.as_view(template_name='login/log_and_signup.html')),


    #url(r'^(?P<ida>[a-z]+)$', views.idcheck, name='id'),
]
