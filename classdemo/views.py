from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class RegisterView(View):

    def get(self, request):
        '''该类视图中的get函数'''

        print('RegisterView get')

        return HttpResponse('RegisterView get')

    def post(self, request):
        '''该类视图中的post函数'''

        print('RegisterView post')

        return HttpResponse('RegisterVIew post')