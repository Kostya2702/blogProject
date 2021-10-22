from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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


# def popular(request):
#     questions_set_pop = Question.objects.popular()
#     paginator = Paginator(questions_set_pop, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'qa/popular.html', {'page_obj': page_obj, 'menu': menu})


class QuestionPage(DetailView):
    model = Question
    template_name = 'qa/question.html'
    # form_class = AnswerForm
    context_object_name = 'quest_page'
    #
    # def get_success_url(self):
    #     # return reverse('question', kwargs={'quest_id': self.object.pk})
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_object()
        # context['answers'] = self.object.quest_page.filter(question=question)
        return context
    #
    # def get_initial(self):
    #     return {'event': self.get_object()}

    # def post(self, *args, **kwargs):
    #     self.object = self.object()
    #     form = self.get_form()
    #
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # def form_valid(self, form):
    #     new_answer = form.save(commit=False)
    #     new_answer.question = self.object()
    #     new_answer.save()
    #     return super().form_valid(form)
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


class ShowAskForm(DataMixin, CreateView):
    form_class = AskForm
    template_name = 'qa/ask.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='Задать question')
        return dict(list(context.items()) + list(context_mixin.items()))

