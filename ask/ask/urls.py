from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include('qa.urls')),
    url('login/', include('qa.urls')),
    url('signup/', include('qa.urls')),
    url('question/\d+/', include('qa.urls')),
    url('ask/', include('qa.urls')),
    path('popular/', include('qa.urls')),
    path('new/', include('qa.urls')),
]
