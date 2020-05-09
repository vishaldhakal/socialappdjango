from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    friends = models.ManyToManyField("Profile",blank=True,related_name='friend')
    slug = models.SlugField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usser')

class friendRequest(models.Model):
    frommm = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='fromm')
    to = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='to')

def create_profile(sender, instance, created, **kwargs):
    if created == False:
        Profile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)

def update_profile(sender, instance, created, **kwargs):
    if created :
        instance.Profile.save()

post_save.connect(update_profile,sender=User)