
from django.urls import path
from . import views
urlpatterns = [
    path("articles/", views.LastArticles.as_view())
]