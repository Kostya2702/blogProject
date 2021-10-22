from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', test, name='login'),
    path('signup/', test, name='signup'),
    path('question/<int:quest_id>/', QuestionPage, name='question'),
    path('ask/', ShowAskForm.as_view(), name='ask'),
    path('popular/', Popular.as_view(), name='popular'),
]
