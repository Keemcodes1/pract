from django.db import models

# Create your models here.

class Products (models.Model):
    name = models.CharField(max_length=200, null= False)
    price = models.IntegerField(default=0.00)
    description = models.TextField(max_length=500, null = True)
    image = models.ImageField(upload_to='products/', null = True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name