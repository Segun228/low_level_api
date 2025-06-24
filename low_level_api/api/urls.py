from django.urls import path
from .views import user_view, user_id_view, post_view, post_id_view, regular_user_view, regular_user_id_view

urlpatterns = [
    path("users/", user_view, name="user-list"),
    path("users/<int:id>/", user_id_view, name="user-detail"),
    path("posts/", post_view, name="post-list"),
    path("posts/<int:id>/", post_id_view, name="post-detail"),
    path("regular_users/", regular_user_view, name="regular-user-list"),
    path("regular_users/<int:id>/", regular_user_id_view, name="regular-user-detail"),
]
