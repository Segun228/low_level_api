from django.urls import path
from .views import user_view, user_id_view

urlpatterns = [
    path("users/", user_view, name="user-list"),
    path("users/<int:id>/", user_id_view, name="user-detail"),
]
