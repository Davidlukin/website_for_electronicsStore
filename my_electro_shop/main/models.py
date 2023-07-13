from django.db import models

class TraidIns(models.Model):
    phone_number = models.CharField(max_length=20)
    state = models.IntegerField()
    model_name = models.CharField(max_length=50)
