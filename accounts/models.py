from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)# 1:N이 아니라 1:1이므로
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
