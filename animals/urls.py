from django.conf.urls import url
from .views import all_animals

urlpatterns = [
    url(r'^$', all_animals, name="all_animals"),
]