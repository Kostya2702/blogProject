from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Популярное', 'url_name': 'popular'},
    {'title': 'Задать вопрос', 'url_name': 'ask'},
    {'title': 'Log in', 'url_name': 'login'},
    {'title': 'Sign-up', 'url_name': 'signup'},
]


class DataMixin:
    paginate_by = 5
    model = Question

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
