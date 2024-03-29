from django.db import models
from django import forms

# Create your models here.

LANGUAGE_CHOICES = (
                    ('한국어','한국어'),
                    ('영어', '영어'),
)

CATEGORY_CHOICES = (
                    ('poem','poem'),
                    ('not_poem', 'not_poem'),
)
class Maratron(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=4, choices=LANGUAGE_CHOICES, default="한국어")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="not_poem")
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.FileField(upload_to='contents', max_length=100)
    audio = models.FileField(upload_to='audio', max_length=100)
    thumnail = models.FileField(upload_to='thumnail', max_length=100)

    def __str__(self):
        return  self.title
    def dic(self) :
        fields = ['id', 'language', 'category', 'author','title', 'contents', 'audio', 'thumnail' ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result