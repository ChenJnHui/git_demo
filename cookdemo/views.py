from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def setcookfunc(request):
    '''设置cookie'''

    # 1.创建response
    response = HttpResponse('setcookfunc')

    # response.set_cookie('key', 'value', '有效期(s)')
    # 如果不设置有效期时间, 浏览器全部关闭,则key&amp;value删除
    response.set_cookie('itcast', 'python', max_age=3600 * 24 * 14)

    return response

def getcookfunc(request):
    '''读取cookie的值'''

    value = request.COOKIES.get('itcast')

    print(value)

    return HttpResponse('getcookfunc')