from django.db import models


class LinkBase(models.Model):
    long = models.CharField(max_length=500)
    short = models.CharField(max_length=30)
    date = models.DateField

    def __str__(self):
        return self.short

# Create your models here.
