from django.db import models

# Create your models here.
class SignupModel(models.Model):
    name=models.CharField(default="",max_length=100)
    image=models.CharField(default="",max_length=500)
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)


class PostModel(models.Model):
    userid=models.CharField(default="",max_length=100)
    title=models.CharField(default="",max_length=100)
    message=models.CharField(default="",max_length=100)
    