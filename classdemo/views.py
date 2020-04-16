from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator


# 定义一个装饰器
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('请求路径: %s' % request.path)
        print('装饰器被调用了')
        return func(request, *args, **kwargs)
    return wrapper

def my_decorator_2(func):
    def wrapper(request, *args, **kwargs):
        print('请求路径2: %s' % request.path)
        print('装饰器被调用了2')
        return func(request, *args, **kwargs)
    return wrapper

class FirstMixin(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return my_decorator(view)

class SecondMixin(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return my_decorator_2(view)

class RegisterView(FirstMixin, SecondMixin, View):

    def get(self, request):
        '''该类视图中的函数'''
        print('RegisterView get')
        return HttpResponse('RegisterView get')

    def post(self, request):
        '''该类视图中的post函数'''
        print('RegisterView post')
        return HttpResponse('RegisterView post')

























# Create your views here.
# class RegisterView(View):
#
#     def get(self, request):
#         '''该类视图中的get函数'''
#
#         print('RegisterView get')
#
#         return HttpResponse('RegisterView get')
#
#     def post(self, request):
#         '''该类视图中的post函数'''
#
#         print('RegisterView post')
#
#         return HttpResponse('RegisterVIew post')