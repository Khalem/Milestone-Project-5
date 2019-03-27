from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=250, blank=False)
    STATUS = (
        ("Critically Endangered", "CE"),
        ("Endangered", "E"),
        ("Vunerable", "V"),
        ("Near Threatened", "NT"),
        ("Least Concern", "LC"),
    )
    status_choices = models.CharField(max_length=30, choices=STATUS, default="Critically Endangered")
    population = models.IntegerField(blank=True, null=True)
    habitat = models.CharField(max_length=250, blank=True, null=True)
    info = models.TextField(blank=False)
    length = models.CharField(max_length=250, blank=True, null=True)
    height = models.CharField(max_length=250, blank=True, null=True)
    weight = models.CharField(max_length=250, blank=True, null=True)
    scientific_name = models.CharField(max_length=250, blank=True, null=True)
    threats = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to="animal_profile_img", blank=False)
    header_img = models.ImageField(upload_to="animal_header_img", blank=False)

    
class AdoptAnimalOne(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=False)

class AdoptAnimalTwo(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=False)
    
class AdoptAnimalThree(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=False)
    
    
@receiver(post_save, sender=Animal)
def create_plan_one(sender, instance, created, **kwargs):
    """
        When a new animal has been created in the database, I will create 3 adoption plans linked to that animal.
    """
    if created:
        AdoptAnimalOne.objects.create(
            animal=instance, 
            plan_name="{0} Basic Pack".format(instance.name.title()), 
            price=5.00, 
            description="To thank you for purchasing the {0} Basic Pack, you will recieve a postcard of your {0}!".format(instance.name.title())
        )
        
        AdoptAnimalTwo.objects.create(
            animal=instance, 
            plan_name="{0} Mega Pack".format(instance.name.title()), 
            price=20.00, 
            description="You will recieve the {0} Basic Pack, along with a {0} Keychain and {0} socks!".format(instance.name.title())
        )
        
        AdoptAnimalThree.objects.create(
            animal=instance, 
            plan_name="{0} Ultimate Pack".format(instance.name.title()), 
            price=45.00, 
            description="You will recieve the {0} Starter Pack, along with a {0} Teddy Bear and a framed photo of your {0}!".format(instance.name.title())
        )
        


@receiver(post_save, sender=Animal)
def save_plan_one(sender, instance, **kwargs):
    instance.adoptanimalone.save()
    instance.adoptanimaltwo.save()
    instance.adoptanimalthree.save()