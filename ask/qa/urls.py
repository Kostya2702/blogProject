from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_questions, name='home'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:quest_id>/', views.question_page, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.popular_post, name='popular')
]
