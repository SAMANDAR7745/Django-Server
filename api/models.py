# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
