from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    image = models.ImageField(upload_to='items/', default='items/127826165_p0_master1200.jpg', blank=True, null=True)

    def __str__(self):
        return self.name
