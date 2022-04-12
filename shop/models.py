from django.db import models
from uuid import uuid4


class Food(models.Model):
    id = models.CharField(max_length=300, default=uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='foods')

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    id = models.CharField(max_length=300, default=uuid4, primary_key=True)
    foods = models.ManyToManyField(Food)
    data = models.JSONField()

    def __str__(self) -> str:
        return f"{self.id}"
