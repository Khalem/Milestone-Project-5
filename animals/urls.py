from django.conf.urls import url
from .views import all_animals, animal_detail, up_vote_comment

urlpatterns = [
    url(r'^$', all_animals, name="all_animals"),
    url(r'^(?P<pk>\d+)$', animal_detail, name="animal_detail"),
    url(r'^upvote/(?P<pk>\d+)/(?P<page_id>\d+)', up_vote_comment, name="up_vote_comment"),
]