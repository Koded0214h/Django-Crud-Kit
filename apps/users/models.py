from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pictures/8.png', blank=True, null=True)
    
    groups = models.ManyToManyField(Group, related_name='Customuser_set', blank=True)
    
    user_permissions = models.ManyToManyField(Permission, related_name='CustomUser_permissions_set', blank=True)

    def __str__(self):
        return self.username