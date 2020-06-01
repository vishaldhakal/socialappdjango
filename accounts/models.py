from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import manager



class Profile(models.Model):
    friends = models.ManyToManyField("Profile",blank=True,related_name='friend')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usser')
    cover_photo = models.ImageField(blank=True,null=True)
    profile_photo = models.ImageField(blank=True,null=True)
    profession = models.CharField(max_length=400,blank=True)
    temporary_address = models.CharField(max_length=400,blank=True)
    permanent_address = models.CharField(max_length=400,blank=True)
    contact_no = models.CharField(max_length=400,blank=True)
    bio = models.TextField(blank=True)



class friendRequest(models.Model):
    frommm = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='fromm')
    to = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='to')

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    Profile.objects.update_or_create(user=instance)