from django.urls import path, include

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("about", views.about, name="about"),
   path("process_text", views.process_text, name="process_text"),
   path("process_db", views.process_db, name="process_db"),
   path("test_process_text", views.test_process_text, name="test_process_text"),
   path("test_process_db", views.test_process_db, name="test_process_db"),
   path("test_model", views.test_model, name="test_model"),
   path('accounts/', include('django.contrib.auth.urls')),
]

