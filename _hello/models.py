from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.charField(max_length=255, 'date created', auto_now_add=True)
