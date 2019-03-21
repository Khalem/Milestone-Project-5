from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


class UserLoginForm(forms.Form):
    """
        Form to be used to log in users
    """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(UserCreationForm):
    """
        Form used to register a new user
    """
    
    password1 = forms.CharField(
                label="Password",
                widget=forms.PasswordInput)
    password2 = forms.CharField(
                label="Password Confirmation", 
                widget=forms.PasswordInput)
                
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
            
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        
        return password2
    
class EditProfileForm(forms.ModelForm):
    """
        Form to edit bio and image in user profile
    """
    class Meta:
        model = Profile
        fields = ("bio", "image")
        
    def clean_image(self):
        image = self.cleaned_data.get("image")
            
        if image:
            w, h = get_image_dimensions(image)
            if w != h or w < 200 or w > 400:
                raise forms.ValidationError("The image must have an equal width and height between 200px to 400px!")
            return image
    