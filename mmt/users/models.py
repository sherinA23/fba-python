from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    role = models.CharField(max_length=10, blank=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_set',
        related_query_name='user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
 
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users_set',
        related_query_name='user',
        blank=True,
        help_text='Specific permissions for this user.',
    )
