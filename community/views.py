from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_comments.models import Comment
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """
        Create view that will return a list of posts - I decided upon having 2 seperate types of posts: staff and user. They will each have their own pagination.
    """
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    
    staff_posts = posts.filter(user__is_staff=True)
    user_posts = posts.filter(user__is_staff=False)
    print(user_posts.count())
    
    staff_paginator = Paginator(staff_posts, 4)
    user_paginator = Paginator(user_posts, 4)
    
    # To have the pagination to work seperately to eachother, I will name each page something unique not to return the same page for both staff and users
    staff_page = request.GET.get("staff_page")
    user_page = request.GET.get("user_page")
    
    # Staff Paginate
    try:
        staff_posts = staff_paginator.page(staff_page)
    except PageNotAnInteger:
        staff_posts = staff_paginator.page(1)
    except EmptyPage:
        staff_posts = staff_paginator.page(staff_paginator.num_pages)
        
    # User Paginate
    try:
        user_posts = user_paginator.page(user_page)
    except PageNotAnInteger:
        user_posts = user_paginator.page(1)
    except EmptyPage:
        user_posts = user_paginator.page(user_paginator.num_pages)

    return render(request, "community.html", {"staff_posts": staff_posts, "user_posts": user_posts, "user_page": user_page, "staff_page": staff_page})
 
    
def post_detail(request, pk):
    """
        Create a view that returns a single post object based on the post id
    """
    
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "community-post.html", {"post": post})
    
    
@login_required()
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
    
    
@login_required()    
def up_vote_post_comment(request, pk, page_id):
    """
        This view will check if user has already up voted, then add or remove up vote accordinly - For post comments
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
    
    return redirect("post_detail", page_id)
    
    
    
@login_required()
def up_vote_post(request, pk):
    """
        This view will check if user has already up voted, then add or remove up vote accordinly - For posts
    """
    post = Post.objects.get(pk=pk)
    
    if request.user not in post.postupvote.up_voted.all():
        post.postupvote.up_voted.add(request.user)
        post.postupvote.score += 1
        post.postupvote.save()
    else:
        post.postupvote.up_voted.remove(request.user)
        post.postupvote.score -= 1
        post.postupvote.save()
    
    return redirect("post_detail", pk)