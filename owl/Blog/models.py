from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500, blank=True)
    location=models.CharField(max_length=30, blank=True )
    birthday=models.DateField(null=True, blank=True)


class Post(models.Model):
    Author =models.ForeignKey(Profile,on_delete=models.CASCADE)
    title =models.CharField(max_length=200)
    text = models.TextField()
    # image = models.ImageField(upload_to="./image",null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)