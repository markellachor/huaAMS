from api import views
from django.urls import path

urlpatterns = [
    # Users
    path("login", views.LoginView.as_view(http_method_names=["post"])),
    path("me", views.LoginView.as_view(http_method_names=["get"])),
    path(
        "users/<int:id>",
        views.UsersView.as_view(http_method_names=["get", "delete", "patch"]),
    ),
    path("users", views.UsersView.as_view(http_method_names=["get", "post"])),
    # Departments
    path(
        "departments", views.DepartmentsView.as_view(http_method_names=["get", "post"])
    ),
    path(
        "departments/<int:id>",
        views.DepartmentsView.as_view(http_method_names=["get", "delete", "patch"]),
    ),
    # Buildings
    path("buildings", views.BuildingsView.as_view(http_method_names=["get", "post"])),
    path(
        "buildings/<int:id>",
        views.BuildingsView.as_view(http_method_names=["get", "delete", "patch"]),
    ),
    # Research programs
    path(
        "research-programs",
        views.ResearchProgramsView.as_view(http_method_names=["get", "post"]),
    ),
    path(
        "research-programs/<int:id>",
        views.ResearchProgramsView.as_view(
            http_method_names=["get", "delete", "patch"]
        ),
    ),
    # Research programs
    path(
        "assets",
        views.AssetView.as_view(http_method_names=["get", "post"]),
    ),
    path(
        "assets/<int:id>",
        views.AssetView.as_view(http_method_names=["get", "delete", "patch"]),
    ),
    path(
        "assets/invoice",
        views.FileUploadAPIView.as_view(http_method_names=["post"]),
    ),
    path(
        "assets/invoice/<int:id>",
        views.FileUploadAPIView.as_view(http_method_names=["get"]),
    )
]
