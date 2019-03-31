from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """
        Create view that will return a list of posts
    """
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    return render(request, "community.html", {"posts": posts})
    
def post_detail(request, pk):
    """
        Create a view that returns a single post object based on the post id
    """
    
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "community-post.html", {"post": post})
    
def create_or_edit_post(request, pk=None):
    """
        Create a view that allows us to create or edit, depending if the post id is null or not.
    """
    
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            user = get_object_or_404(User, username=request.user)
            post = Post(user=user, title=request.POST["title"], content=request.POST["content"])
            post.save()
            
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, "community-post-new.html", {"form": form})
    

def delete_post(request, pk):
    """
        Delete a particular post
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    
    return redirect(get_posts)