from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Популярное', 'url_name': 'popular'},
    {'title': 'Задать вопрос', 'url_name': 'ask'},
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Sign-up', 'url_name': 'signup'},
]


class DataMixin:
    model = Question
    context_object_name = 'page_obj'

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
