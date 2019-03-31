from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver

class Post(models.Model):
    """
        A single community post
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
        
        
class PostUpVote(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    score = models.IntegerField(blank=False, null=False)
    up_voted = models.ManyToManyField(User)
    
    
@receiver(post_save, sender=Post)
def create_up_vote(sender, instance, created, **kwargs):
    """
        Each time a post is created, I will create an up vote system
    """
    if created:
        PostUpVote.objects.create(post=instance, score=0)
        
        
@receiver(post_save, sender=Post)
def save_up_vote(sender, instance, **kwargs):
    """
        Save new object.
    """
    instance.postupvote.save()