from django.db import models
from django.contrib.auth import get_user_model
from pytz import timezone

# Create your models here.
User = get_user_model()

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
