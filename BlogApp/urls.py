from django.conf.urls import url, include
from django.contrib import admin
from posts import urls as postUrls
from django.conf import settings
from accounts import urls as cuentasUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.Home.as_view(), name="home"),
   	url(r'^blog/',include(postUrls,namespace="posts")),
    url(r'^accounts/',include(cuentasUrls)),
]
