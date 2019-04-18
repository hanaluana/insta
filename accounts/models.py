from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)# 1:N이 아니라 1:1이므로
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = ProcessedImageField(
        blank=True,
        processors = [Thumbnail(250, 250)],
        options = {'quality': 90}
    )

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'followings', blank=True)