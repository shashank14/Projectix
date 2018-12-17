from django.conf.urls import url
from .views import (get_blog_posts, post_detail_view,post_detail_views,post_like_view)

urlpatterns = [
url(r'^$',get_blog_posts,name='home'),
url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',post_detail_views,name='detail'),
url(r'^(?P<id>\d+)/$',post_detail_view,name='detail'),
url(r'^(?P<id>\d+)/share/$',post_like_view,name='like'),
]
