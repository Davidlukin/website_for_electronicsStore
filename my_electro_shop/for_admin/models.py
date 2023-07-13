from django.db import models

# Create your models here.
class Card_with_description(models.Model):
    title = models.CharField('Название', max_length=150)
    image = models.ImageField(upload_to='images/')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Описание')

    def __str__(self):
        return self.title
