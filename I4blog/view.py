from django.http import HttpResponse
from django.shortcuts import render
from IImodel.models import i4Article


def hello(request):
    context = {}
    context['hello'] = 'Are you FIRST_DAY_OF_WEEKly'
    return render(request, 'hello.html', context)


def dbtest(request):
    ati = i4Article(name='i4b')
    ati.save()
    return HttpResponse("<h1>添加成功</h1>")
