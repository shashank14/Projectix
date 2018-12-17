from django.conf.urls import url, include
from .views import (login_view, signup_view, settings_view, logout_view)


urlpatterns = [
    url(r'^$',login_view,name='login'),
    url(r'^logout$',logout_view,name='logout'),
    url(r'^signup$',signup_view,name='signup'),
    url(r'^settings$',settings_view,name='settings'),
]
