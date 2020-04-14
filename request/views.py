from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

# Create your views here.
def queryfunc(request):
    '''获取前端传入的查询字符串参数'''

    # 获取参数
    queryDict = request.GET

    # 从特殊的dict中获取数据
    a = queryDict.get('a')
    b = queryDict.get('b')
    alist = queryDict.getlist('a')

    # 打印
    print(a)
    print(b)
    print(alist)

    return HttpResponse('queryfunc')

def routerfunc(request, city, year):
    '''获取前端传入的路径参数'''

    print(city)

    print(year)

    return HttpResponse('routerfunc')

def formfunc(request):

    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')

    print(a)
    print(b)
    print(alist)

    return HttpResponse('fromfunc')

def jsonfunc(request):
    ''' json传参'''

    dict = json.loads(request.body.decode())

    a = dict.get('a')
    b = dict.get('b')

    print(a)
    print(b)

    # 演示: 获取请求头信息
    print(request.META.get('CONTENT_LENGTH'))

    # 演示： path, user, method
    print(request.user)
    print(request.path)
    print(request.method)

    response = HttpResponse('jsonfunc')

    response['itcast'] = 'python'

    return response

def responsefunc(request):
    '''响应部分'''
    print('responsefunc')

    return HttpResponse('responsefunc', status=404)

def jsonFunc(request):
    '''讲解JsonResponse类'''

    print('jsonFunc')

    list = [{
        'name':'zs',
        'age':123
    }]

    return JsonResponse(list, safe=False)