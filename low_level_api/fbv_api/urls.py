from django.urls import path
from .views import post_view, post_id_view, regular_user_view, regular_user_id_view

urlpatterns = [
    path("posts/", post_view, name="post-list"),
    path("posts/<int:id>/", post_id_view, name="post-detail"),
    path("regular_users/", regular_user_view, name="regular-user-list"),
    path("regular_users/<int:id>/", regular_user_id_view, name="regular-user-detail"),
]