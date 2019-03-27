from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_comments.models import Comment
from .models import Animal

# Create your views here.
def all_animals(request):
    """
        This view will get all objects from animals and paginate them displaying 8 at a time.
    """
    animals = Animal.objects.all()
    paginator = Paginator(animals, 8)
    
    page = request.GET.get("page")
    
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
    

def up_vote_comment(request, pk, page_id):
    """
        This view will check if user has already up voted, then add or remove up vote accordinly.
    """
    comment = Comment.objects.get(pk=pk)
    
    if request.user not in comment.upvote.up_voted.all():
        comment.upvote.up_voted.add(request.user)
        comment.upvote.score += 1
        comment.upvote.save()
    else:
        comment.upvote.up_voted.remove(request.user)
        comment.upvote.score -= 1
        comment.upvote.save()
    
    return redirect("animal_detail", page_id)