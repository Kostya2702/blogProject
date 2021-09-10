from ask.django import url
from ask.django import admin
from ask.django import include

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
