from django.shortcuts import render
from animals.models import Animal

# Create your views here.
def data(request):
    """
        This view will get some data from the database and then pass the data through for chart.js
    """
    animals = Animal.objects.all()
    
    # Get the amount of objects under a certain population
    length_500 = Animal.objects.filter(population__lte=500).count()
    length_1k = Animal.objects.filter(population__gt=500, population__lte=1000).count()
    length_5k = Animal.objects.filter(population__gt=1000, population__lte=5000).count()
    length_10k = Animal.objects.filter(population__gt=5000, population__lte=10000).count()
    length_over_10k = Animal.objects.filter(population__gt=1000).count()
    
    # Get the amount of objects that have a certain endangered status
    critically = Animal.objects.filter(status_choices="Critically Endangered").count()
    endangered = Animal.objects.filter(status_choices="Endangered").count()
    near_threatened = Animal.objects.filter(status_choices="Near Threatened").count()
    vulnerable = Animal.objects.filter(status_choices="Vunerable").count()
    least_concern = Animal.objects.filter(status_choices="Least Concern").count()
    
    return render(request, "data.html", {"length_500": length_500, "length_1k": length_1k, 
                                        "length_5k": length_5k, "length_10k": length_10k, 
                                        "length_over_10k": length_over_10k, 
                                        "critically": critically, "endangered": endangered,
                                        "near_threatened": near_threatened, "vulnerable": vulnerable,
                                        "least_concern": least_concern
                })