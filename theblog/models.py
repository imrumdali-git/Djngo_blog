from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Catogery(models.Model):    #Category spelling mistake
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))     #This coding direct goes to required new Post
        return reverse('home')
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    catogery = models.CharField(max_length= 255, default ='coding')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))     #This coding direct goes to required new Post
        return reverse('home')