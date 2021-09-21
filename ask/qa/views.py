from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    questions_set = Question.objects_new.new()
    paginator = Paginator(questions_set, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'page_obj': page_obj, 'title': 'Новое'})


def popular_post(request):
    pop_questions_set = Question.objects_new.new()
    paginator = Paginator(pop_questions_set, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/popular.html', {'page_obj': page_obj, 'title': 'Новое'})
