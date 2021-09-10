from django.conf.urls import url
from django.contrib import admin
from django.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('qa.urls')),
    url('login/', include('qa.urls')),
    url('signup/', include('qa.urls')),
    url('question/<27>/', include('qa.urls')),
    url('ask/', include('qa.urls')),
    url('popular/', include('qa.urls')),
    url('new/', include('qa.urls')),
]
