from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.new_questions, name='home'),
    url('^login/$', views.test, name='login'),
    url('^signup/$', views.test, name='signup'),
    url('^question/<int:quest_id>/$', views.question_page, name='question'),
    url('^ask/$', views.test, name='ask'),
    url('^popular/$', views.popular_post, name='popular')
]
