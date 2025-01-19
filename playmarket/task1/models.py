from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=30)
    age = models.DecimalField(decimal_places=0, max_digits=3)


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    size = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.TextField()
    age_limited = models.BooleanField()
    buyer = models.ManyToManyField(Buyer, related_name='games')


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
