from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.new_questions),
    url('login/', views.test),
    url('signup/', views.test),
    url('question/\d+/', views.test),
    url('ask/', views.test),
    url('popular/', views.test),
    url('new/', views.test)
]