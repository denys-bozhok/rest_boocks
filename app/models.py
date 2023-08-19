from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.

class Boock(models.Model):
    tittle = models.CharField(max_length = 30, unique=True)
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    description = models.TextField()
    date = models.CharField(max_length = 30)
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tittle)
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f'{self.tittle}'
        