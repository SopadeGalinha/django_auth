from django.urls import path, include
from .views import authView, home

app_name = "accounts"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="signup"),
    path("login/", include("django.contrib.auth.urls")),  # Changed this line
]
