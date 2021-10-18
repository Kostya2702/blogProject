from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    questions_set = Question.objects.new()
    paginator = Paginator(questions_set, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'page_obj': page_obj, 'title': 'Новое'})


def popular(request):
    questions_set_pop = Question.objects.popular()
    paginator = Paginator(questions_set_pop, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/popular.html', {'page_obj': page_obj, 'title': 'Популярное'})


def question(request, quest_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            return redirect(form.save())
    else:
        AnswerForm()

    quest_page = get_object_or_404(Question, pk=quest_id)
    answers = Answer.objects.filter(question=quest_id)
    return render(request, 'qa/question.html', {'quest_page': quest_page, 'answers': answers})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            return redirect(form.save())
    else:
        form = AskForm()

    return render(request, 'qa/ask.html', {'form': form, 'title': 'Задать вопрос'})
