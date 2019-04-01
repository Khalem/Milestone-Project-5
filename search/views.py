from django.shortcuts import render
from animals.models import Animal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def search_animals(request):
    """
        This view will allow users to search through the animals in the database based on their name and endangered status
    """
    page = request.GET.get("page")
    
    # Checking which input was filled
    if request.GET["q"] and request.GET["status"]:
        animals = Animal.objects.filter(name__icontains=request.GET["q"])
        animals = animals.filter(status_choices=request.GET["status"])
    elif request.GET["q"]:
        animals = Animal.objects.filter(name__icontains=request.GET["q"])
    elif request.GET["status"]:
        animals = Animal.objects.filter(status_choices=request.GET["status"])
    
    paginator = Paginator(animals, 8)
    
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
        
    
    # In order for pagination to keep the users search parameters when they change page, I need to create a custom url to pass as a variable into the template
    custom_url = "?status={0}&q={1}".format(request.GET["status"].replace(" ", "+"), request.GET["q"].replace(" ", "+"))
        
    return render(request, "animals.html", {"animals": animals, "custom_url": custom_url})
    
    
    