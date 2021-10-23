from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('accounts/login/', test, name='login'),
    path('accounts/logout/', test, name='logout'),
    path('signup/', test, name='signup'),
    path('question/<int:quest_id>/', QuestionPage.as_view(), name='question'),
    path('ask/', ShowAskForm.as_view(), name='ask'),
    path('popular/', Popular.as_view(), name='popular'),
]
