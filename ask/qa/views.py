from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from ask.qa.models import QuestionManager


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    question_list = QuestionManager.all()
    # limit = request.GET.get('limit', 10)
    paginator = Paginator(question_list.new, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'post': page_obj})


def popular_post(request):
    pop_post_list = QuestionManager.all()
    # limit = request.GET.get('limit', 10)
    paginator = Paginator(pop_post_list.popular, 10)
    page_number = request.GET.get('page')
    page_obj_pop = paginator.get_page(page_number)
    return render(request, 'qa/popular.html', {'post': page_obj_pop})
