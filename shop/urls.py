from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^foods/', views.Foods.as_view()),
    re_path(r'^newOrder/', views.Orders.as_view()),
]
