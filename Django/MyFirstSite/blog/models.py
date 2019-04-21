from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    createTime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    content = models.TextField()

class Comment(models.Model): # 在 db 內新增 Comment 的 table
    # 不用建 id，id 自動會有
    name = models.CharField(max_length=50) # 新增一個 char(50) 的欄位 name
    content = models.TextField() # 新增一個 text 的欄位 cotent
    createTime = models.DateTimeField(auto_now_add=True) # 新增一個時間欄位，而當資料被 create 時，這筆資料的 createTime 會存當下的時間
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )