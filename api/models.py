from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):   # function string
        return self.name #self like "this" in oop

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.FloatField()
    description = models.TextField(blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
     return self.name