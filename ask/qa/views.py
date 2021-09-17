from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    question_list = Question.objects_new.new()
    # limit = request.GET.get('limit', 10)
    paginator = Paginator(question_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'post': page_obj})


def popular_post(request):
    pop_post_list = Question.objects_new.popular()
    # limit = request.GET.get('limit', 10)
    paginator = Paginator(pop_post_list, 10)
    page_number = request.GET.get('page')
    page_obj_pop = paginator.get_page(page_number)
    return render(request, 'qa/popular.html', {'post': page_obj_pop})
