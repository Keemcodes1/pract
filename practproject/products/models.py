from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Products (models.Model):
    user =models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null= False, default='No name')
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    description = models.TextField(max_length=500, null = True, blank=True)
    inventory = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null = True, blank=True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    def has_inventory(self):
        return self.inventory > 0
        

    def __str__ (self):
        return self.title