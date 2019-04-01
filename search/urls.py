from django.conf.urls import url
from .views import search_animals

urlpatterns = [
    url(r'^$', search_animals, name="search_animals"),    
]