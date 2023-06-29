from django.urls import path

from .views import ComplaintCreateView, ComplaintDetailView, ComplaintListView

urlpatterns = [
    path("", ComplaintListView.as_view(), name="complaint-list"),
    path("detail/<int:pk>/", ComplaintDetailView.as_view(), name="complaint-detail"),
    path("new/", ComplaintCreateView.as_view(), name="complaint-create"),
]
