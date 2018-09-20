from django.urls import path, include

# from . import views
from elo.views import gui_views
from elo.views import api_views

urlpatterns = [
   path("", gui_views.index, name="index"),
   path("about", gui_views.about, name="about"),
   path("get_db", gui_views.get_db, name="get_db"),
   path("get_meta", gui_views.get_meta, name="get_meta"),
   path("insert_db", gui_views.insert_db, name="insert_db"),
   path("search_db", gui_views.search_db, name="search_db"),
   path("delete_db", gui_views.delete_db, name="delete_db"),
   path("test_db_template", gui_views.test_db_template, name="test_db_template"),
   path("test_model", gui_views.test_model, name="test_model"),
   path("api_", gui_views.api_, name="api_"),
   path("api_get_meta", api_views.api_get_meta, name="api_get_meta"),
   path("api_get_hook/<str:db_hook>", api_views.api_get_hook, name="api_get_hook"),
   path('accounts/', include('django.contrib.auth.urls')),
]

