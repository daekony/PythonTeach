from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.http import HttpResponse

from blog.models import Comment

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def page1(request):
    if request.POST:  # 判斷是否是 POST
        name = request.POST.get("name")
        content = request.POST.get("content")

        comment = Comment.objects.create(  # 在 db 內新增一筆 Comment
            name=name,
            content=content,
        )

    context = {
        "comments": Comment.objects.all() # select * from Comment;
    }
    return render(request, 'blog/page1.html', context)


def login(request):
    if request.POST:
        # 當使用者 POST 表單後運行這部分程式碼
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 用 auth.authenticate 來找 db 內是否有這筆帳戶資料
        user = auth.authenticate(username=username, password=password)
        
        if user and user.is_active: # 判斷 user 是否存在，且沒有被凍結
            # 允許登入
            auth.login(request, user)
            return redirect(reverse_lazy('index')) # 進行導頁到 index
        else:     
            # 不允許登入
            context = {
                "msg": "登入失敗",
            }
            return render(request, 'blog/login.html', context)

    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return redirect(reverse_lazy('index'))  # 登出後導頁到 index 


def register(request):
    if request.POST:
        # 當使用者 POST 表單後運行這部分程式碼
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if not User.objects.filter(username=username).exists(): # 判斷是否 username 有存在 db 內
                user = User.objects.create(
                    username=username,
                    password=make_password(password1), # 密碼加密
                )
                return redirect(reverse_lazy('login'))  # 登出後導頁到 login
            else:
                context = {
                    "msg": "此使用者帳號已被申請過",
                }
                return render(request, 'blog/register.html', context)
        else:
            context = {
                "msg": "一次密碼與二次密碼不相同",
            }
            return render(request, 'blog/register.html', context)
    return render(request, 'blog/register.html')
