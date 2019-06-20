from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=254, default='')
    address_1 = models.CharField(max_length=254, default='')
    address_2 = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    state = models.CharField(max_length=30, default='')
    zip_code = models.CharField(max_length=5, default='')
   

    def __str__(self):
        return f'{self.user.username} Profile'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
