from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    text = models.TextField()
    date = models.CharField(max_length = 30)
        
    def __str__(self) -> str:
        return f'{self.user}'
        