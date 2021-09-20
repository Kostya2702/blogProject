from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_questions),
    url('login/', views.test, name='home'),
    url('signup/', views.test),
    url('question/\d+/', views.test),
    url('ask/', views.test),
    path('popular/', views.popular_post),
    path('new/', views.test)
]