from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('qa.urls')),
    path('login/', include('qa.urls')),
    path('signup/', include('qa.urls')),
    path('question/\d+/', include('qa.urls')),
    path('ask/', include('qa.urls')),
    path('popular/', include('qa.urls')),
    path('new/', include('qa.urls')),
]
