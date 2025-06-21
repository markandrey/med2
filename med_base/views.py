from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Test


def test_list(request):
    tests = Test.objects.all()
    return render(request,
                  'med_base/list.html',
                  {'tests': tests})


def one_test(request, id):
    test = get_object_or_404(Test, id=id)

    return render(request,
                  'med_base/detail.html',
                  {'test': test})


def index(request):
    return render(request, 'base.html')


def about(request):
    return HttpResponse(f'<h2>О пользователе</h2>')


def contact(request):
    return HttpResponse('<h2>Контакты</h2>')
