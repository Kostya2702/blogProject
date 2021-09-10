from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url('', test),
    url('login/', test, name='login'),
    url('signup/', test, name='signup'),
    url('question/<27>/', test, name='question'),
    url('ask/', test, name='ask'),
    url('popular/', test, name='popular'),
    url('new/', test, name='new'),
]
