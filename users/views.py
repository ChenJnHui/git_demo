from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def haha(request):

    print('haha 函数')

    return HttpResponse('haha函数')

def index(request):

    print('index 函数')

    return HttpResponse('index函数')

def say(request):

    print('say 函数')
    url = reversed('uu:index')
    print(url)

    # return HttpResponse('say函数')
    return redirect(url)
