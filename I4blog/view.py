from django.shortcuts import render
from IImodel.models import i4Article
from django.http import HttpResponse
from Spider import newsSpider


def hello(request):
    context = {}
    context['hello'] = newsSpider().getNews()
    return render(request, 'frame.html', context)


def dbtest(request):
    ati = i4Article(name='i4b')
    ati.save()
    return HttpResponse("<h1>添加成功</h1>")


def menu(request):
    context = {}
    return render(request, 'menu.html', context)

