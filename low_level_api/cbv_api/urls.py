from django.urls import path
from .views import StudentListView, StudentDetailView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student-detail"),
]