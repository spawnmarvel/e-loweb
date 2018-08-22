from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("about", views.about, name="about"),
   path("get_user_text", views.get_user_text, name="get_user_text"),
]
