from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= 'profile')
    description = models.CharField(max_length = 100, null= True, blank = True)
    link =  models.CharField(max_length = 500, null= True, blank = True)
    profile_picture = models.ImageField(upload_to = 'profile_pictures',null= True, blank = True)
