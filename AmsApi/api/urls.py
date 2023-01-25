from api import views
from django.urls import path

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('me', views.UserView.as_view())
]