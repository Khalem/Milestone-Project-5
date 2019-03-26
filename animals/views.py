from django.shortcuts import render
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