from django.urls import path
from . import views

urlpatterns = [
    path("followers/", views.Followers.as_view()),
    path("following/", views.Following.as_view()),
]
