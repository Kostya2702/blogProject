from django import url, incude
from django import admin
from qa import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', views.test),
    url('^login/$', views.test),
    url('^signup/$', views.test),
    url('^question/\d+/$', views.test),
    url('^ask/$', views.test),
    url('^popular/.', views.test),
    url('^new/$', views.test),
]
