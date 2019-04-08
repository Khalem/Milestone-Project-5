from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post, delete_post, up_vote_post_comment, up_vote_post

urlpatterns = [
    url(r'^$', get_posts, name="get_posts"),
    url(r'^(?P<pk>\d+)$', post_detail, name="post_detail"),
    url(r'^new/$', create_or_edit_post, name="new_post"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name="edit_post"),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name="delete_post"),
    url(r'^post_upvote/(?P<pk>\d+)/', up_vote_post, name="up_vote_post"),
    url(r'^post-upvote-comment/(?P<pk>\d+)/(?P<page_id>\d+)', up_vote_post_comment, name="up_vote_post_comment"),
]