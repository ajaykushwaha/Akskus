
from django.conf.urls import url
from django.contrib import admin
from lsearch import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lsearch',views.search,name='kkk'),
    url(r'^search/$',views.get_search,name='get'),
]
