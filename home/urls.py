from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.handleSignUp, name="handleSignUp"),
    path("loginPage", views.loginPage, name="loginPage"),
    path("log", views.handeLogin, name="handeLogin"),
    path("logout", views.handelLogout, name="handelLogout"),
    path("profile", views.myprofile, name="myprofile"),
    path("makepost", views.makepost, name="makepost"),
    path("update", views.update, name="update"),
    path("profile/<str:username>", views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
