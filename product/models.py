from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import User
class product(models.Model):
    title=models.CharField(max_length=250)
    votes_total=models.IntegerField(default=1)
    body=models.TextField()
    url=models.TextField()
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)
    def summary(self):
        return self.body[:100]
    
    def __str__(self):
        return self.title
class blog(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    qualification=models.TextField()
    country=models.TextField()
    phone_no=models.IntegerField()
