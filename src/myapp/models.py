from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    no_of_files = models.IntegerField()
    date_joined = models.DateField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='user_images', default='user_images/default_profile.jpg')
    
    
class file_upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    type = models.CharField(blank=True)
    file = models.FileField(upload_to="files")
    file_name = models.CharField(blank=True, max_length=50)
    created = models.DateField(auto_now=False, auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)