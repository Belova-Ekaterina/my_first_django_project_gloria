from django.urls import path
from app import views

urlpatterns = [
    path("main-page/", views.index, name="index")
]