from django.db import models
from django import forms

# Create your models here.

CATEGORY_CHOICES = (
                    ('song','Song'),
                    ('poem', 'Poem'),
)
class Maratron(models.Model):
    index = models.AutoField(primary_key=True)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default="song")
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.FileField(upload_to='contents', max_length=100)
    audio = models.FileField(upload_to='audio', max_length=100)

    def __str__(self):
        return  self.title