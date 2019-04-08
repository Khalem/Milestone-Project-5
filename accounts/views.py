from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, EditProfileForm
from .models import Profile
from community.models import Post

# Create your views here.
def index(request):
    """
        Return the index.html file
    """
    return render(request, "index.html")

@login_required    
def logout(request):
    """
        Log the user out
    """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """
        Return a login page
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password"])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse("index"))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
    

def registration(request):
    """
        Render the registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST["username"],
                                     password=request.POST["password1"])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse("index"))
            else:
                messages.error(request, "Unable to register your account at this time")
                
    else:
        registration_form = UserRegistrationForm()
    
    return render(request, "registration.html", 
                {"registration_form": registration_form})


@login_required
def edit_profile(request):
    """
        Allow users to edit the bio and image of their profile.
    """

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            user_profile = form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect(profile)
    else:
        form = EditProfileForm(instance=request.user.profile)
        
    return render(request, "edit-profile.html", {"form": form})

               
def profile(request, pk):
    """
        The users profile page - I will get all posts created by user (if they have any) and then paginate it.
    """
    user = User.objects.get(pk=pk)
    user_posts = Post.objects.filter(user=user).order_by("-published_date")
    

    paginator = Paginator(user_posts, 4)

    page = request.GET.get("page")

    # Paginate
    try:
        user_posts = paginator.page(page)
    except PageNotAnInteger:
        user_posts = paginator.page(1)
    except EmptyPage:
        user_posts = paginator.page(paginator.num_pages)
    
    
    return render(request, "profile.html", {"user_profile": user, "user_posts": user_posts })