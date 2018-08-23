from django.urls import path, include

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("about", views.about, name="about"),
   path("process_text", views.process_text, name="process_text"),
   path("process_db", views.process_db, name="process_db"),
   path('accounts/', include('django.contrib.auth.urls')),
]
