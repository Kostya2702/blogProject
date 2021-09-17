from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('qa.urls')),
    url('login/', include('qa.urls')),
    url('signup/', include('qa.urls')),
    url('question/\d+/', include('qa.urls')),
    url('ask/', include('qa.urls')),
    url('popular/', include('qa.urls')),
    url('new/', include('qa.urls')),
]
