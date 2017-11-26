from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
	context ={}
	context['hello']='Are you FIRST_DAY_OF_WEEKly'
	return render(request,'hello.html',context)