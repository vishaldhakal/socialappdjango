from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    title = models.TextField()
    description = models.TextField()
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')

    def __self__(self):
        return str(self.title)

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)

class  Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)

class messageModel(models.Model):
    userfrom = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userfrom')
    userto = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userto')
    message = models.TextField()


