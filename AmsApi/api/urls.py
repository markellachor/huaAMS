from api import views
from django.urls import path

urlpatterns = [
    # Users
    path("login", views.LoginView.as_view(http_method_names=["post"])),
    path("users/<int:id>", views.UsersView.as_view(http_method_names=["get"])),
    path("users", views.UsersView.as_view(http_method_names=["get", "post"])),
    # Departments
    path(
        "departments", views.DepartmentsView.as_view(http_method_names=["get", "post"])
    ),
    path(
        "departments/<int:id>", views.DepartmentsView.as_view(http_method_names=["get"])
    ),
]
