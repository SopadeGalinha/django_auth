# accounts/urls.py
from django.urls import path, include
from .views import authView, home

app_name = "accounts"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="signup"),
    path("", include("django.contrib.auth.urls")),
]
