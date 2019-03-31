from django.shortcuts import render
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
