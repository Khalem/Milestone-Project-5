from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=750, blank=True)
    image = models.ImageField(upload_to="profile_img", blank=True, null=True)
    adopted = ArrayField(
        base_field=models.TextField(),
        size=100,
        editable="False",
        null=True
        )
    rank = models.CharField(max_length=250, default="Praesidio Member", editable="False")
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    