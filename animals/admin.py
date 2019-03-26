from django.contrib import admin
from .models import Animal, AdoptAnimalOne, AdoptAnimalTwo, AdoptAnimalThree

# Register your models here.
admin.site.register(Animal)
admin.site.register(AdoptAnimalOne)
admin.site.register(AdoptAnimalTwo)
admin.site.register(AdoptAnimalThree)