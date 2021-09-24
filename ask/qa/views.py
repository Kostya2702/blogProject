from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    questions_set = Question.objects.new()
    paginator = Paginator(questions_set, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'page_obj': page_obj, 'title': 'Новое'})


def popular_post(request):
    questions_set = Question.objects.popular()
    paginator = Paginator(questions_set, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/popular.html', {'page_obj': page_obj, 'title': 'Популярное'})


def question_page(request, quest_id):
    quest_page = get_object_or_404(Question, pk=quest_id)
    return render(request, 'qa/question.html', {'quest_page': quest_page})
