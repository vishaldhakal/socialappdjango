from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import manager



class Profile(models.Model):
    friends = models.ManyToManyField("Profile",blank=True,related_name='friend')
    slug = models.SlugField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usser')


class friendRequest(models.Model):
    frommm = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='fromm')
    to = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='to')

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    Profile.objects.update_or_create(user=instance)