from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .models import *
from .forms import *
from .utils import DataMixin


def test(request, *args, **kwargs):
    return HttpResponse('OK')


class HomePage(DataMixin, ListView):
    template_name = 'qa/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='Ne blog')
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_queryset(self):
        return Question.objects.new()


# def index(request):
#     questions_set = Question.objects.new()
#     paginator = Paginator(questions_set, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'qa/index.html', {'page_obj': page_obj, 'title': 'Новое'})


class Popular(DataMixin, ListView):
    template_name = 'qa/popular.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='POPулярное')
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_queryset(self):
        return Question.objects.popular()


class QuestionPage(FormMixin, DataMixin, DetailView):
    template_name = 'qa/question.html'
    pk_url_kwarg = 'quest_id'
    form_class = AnswerForm
    context_object_name = 'quest_page'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title=context['quest_page'])
        context['form'] = self.get_form()
        context['answers'] = self.object.question.filter(question=self.kwargs['quest_id'])
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_initial(self):
        return {'event': self.get_object()}

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_answer = form.save(commit=False)
        new_answer.question = self.get_object()
        new_answer.author = self.request.user
        new_answer.save()
        return super().form_valid(form)


class ShowAskForm(DataMixin, CreateView):
    form_class = AskForm
    template_name = 'qa/ask.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='Задать question')
        return dict(list(context.items()) + list(context_mixin.items()))


# def question(request, quest_id):
#     quest_page = get_object_or_404(Question, pk=quest_id)
#     answers = quest_page.question.filter(question=quest_page)
#
#     # Форма для оставления ответов под вопросами
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#
#             # Создание комментариев
#             new_answer = form.save(commit=False)
#             new_answer.question = quest_page
#             new_answer.save()
#             return redirect(quest_page)
#     else:
#         form = AnswerForm()
#
#     context = {'form': form,
#                'quest_page': quest_page,
#                'answers': answers,
#                'menu': menu
#                }
#
#     return render(request, 'qa/question.html', context=context)



