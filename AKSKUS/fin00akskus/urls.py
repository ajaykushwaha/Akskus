
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('akskus.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^mail/', include('mail.urls'))

]
