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
    context = {
        'title': 'Главная',
        'content': 'Последние редактируемые записи',
    }
    return render(request, 'med_base/index.html', context)


def about(request):
    context = {
        'title': 'О сайте',
        'content': 'О сайте',
        'text_on_page': 'Далеко-далеко за словесными горами в стране, гласных и согласных живут рыбные тексты. Коварный встретил пор, составитель снова собрал даже рукопись от всех? Предупредила буквоград правилами его вдали. Продолжил путь парадигматическая вопроса всеми себя?',
    }
    return render(request, 'med_base/about.html', context)


def contact(request):
    return HttpResponse('<h2>Контакты</h2>')
