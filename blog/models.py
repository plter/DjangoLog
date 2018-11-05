from django.db import models
import datetime


# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=512)
    post_content = models.TextField(null=True)
    post_date = models.DateField(auto_now_add=True, null=True)
