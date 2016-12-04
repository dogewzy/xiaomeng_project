# 想写自己的装饰器,接受login_utl,redirect_url两个参数，还有一个固定参数是no-perm的页面
from django.shortcuts import redirect

login_url = 'http://localhost:8000/polls/login/',
redirect_url = 'http://localhost:8000/polls/no_permission/'


def perm_deco():
    def d1(view_func):
        def d2(request, *args, **kwargs):
            view_func(request, *args, **kwargs)
        return d2
    return d1



