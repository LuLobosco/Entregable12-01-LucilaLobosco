from django.db import models
from django.contrib.auth.models import User

class ImageIndex(models.Model):
    index_picture = models.ImageField(upload_to = 'index_picture',null= True, blank = True)
    name = models.CharField(max_length=50,null= True, blank = True)
#    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name= 'profile')
