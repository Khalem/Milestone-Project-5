from django.conf.urls import url
from .views import data

urlpatterns = [
    url(r'^$', data, name="data")    
]