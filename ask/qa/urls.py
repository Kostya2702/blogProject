from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_questions, name='home'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/\d+/', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.popular_post, name='popular'),
    path('new/', views.test, name='new')
]