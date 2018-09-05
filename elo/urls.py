from django.urls import path, include

from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("about", views.about, name="about"),
   path("get_db", views.get_db, name="get_db"),
   path("get_meta", views.get_meta, name="get_meta"),
   path("insert_db", views.insert_db, name="insert_db"),
   path("search_db", views.search_db, name="search_db"),
   path("delete_db", views.delete_db, name="delete_db"),
   path("test_db_template", views.test_db_template, name="test_db_template"),
   path("test_model", views.test_model, name="test_model"),
   path("test_rest", views.test_rest, name="test_rest"),
   path('accounts/', include('django.contrib.auth.urls')),
]

