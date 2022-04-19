from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name='Категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')

class Post(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="image/")
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,default='Названия Моего Поста')
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    body = models.TextField()
    data = models.DateTimeField(auto_now_add= True)
    categry = models.CharField(max_length=255,default='Без котегория')
    like = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse ('home')
        # return reverse ('article-detail', args=(str(self.id)))


