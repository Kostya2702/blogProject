from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', include('qa.urls')),
]
