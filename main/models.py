from django.db import models
from django.db.models.deletion import CASCADE


class Country(models.Model):
    name = models.CharField(max_length=200, null=True)
    capital = models.TextField()
