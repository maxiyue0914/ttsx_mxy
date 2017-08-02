# coding=utf-8
from django.shortcuts import render, redirect
from hashlib import sha1
from models import user_info


# Create your views here.

def register(request):
    context={'title':'注册'}
    return render(request, 'tt_user/register.html',context)


def register_handle(request):
    dict = request.POST
    uname = dict.get('user_name')

    upwd1 = dict.get('pwd')
    upwd2 = dict.get('cpwd')
    email = dict.get('email')
    if upwd1 != upwd2:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd1)
    upwd_sha1 = s1.hexdigest()

    user = user_info()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = email
    user.save()

    return redirect('/user/login/')


def login(request):
    context={'title':'登录'}
    return render(request, 'tt_user/login.html',context)
