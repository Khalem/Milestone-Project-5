from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Animal

# Create your views here.
def all_animals(request):
    """
        This view will get all objects from animals and paginate them displaying 8 at a time.
    """
    animals = Animal.objects.all()
    paginator = Paginator(animals, 8)
    
    page = request.GET.get("page", 1)
    
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    
    return render(request, "animals.html", {"animals": animals})
    

def animal_detail(request, pk):
    """
        This view will return a specific animal.
    """
    
    animal = get_object_or_404(Animal, pk=pk)
    
    return render(request, "animal-detail.html", {"animal": animal})