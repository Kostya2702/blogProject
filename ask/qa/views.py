from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    question_list = Question.objects_new.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(question_list, limit)
    paginator.baseurl = 'new/?page='
    page_obj = paginator.page(page)
    return render(request, 'qa/index.html', {
        question_list: page_obj.object_list,
        paginator: paginator, page: page_obj,
        'title': 'Новое'
    })


def popular_post(request):
    pop_post_list = Question.objects_new.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(pop_post_list, limit)
    paginator.baseurl = 'new/?page='
    page_obj_pop = paginator.page(page)
    return render(request, 'qa/popular.html', {
        pop_post_list: page_obj_pop.object_list,
        paginator: paginator, page: page_obj_pop,
        'title': 'Популярное'
    })
