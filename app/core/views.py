from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Complaint, ComplaintHandling
from .forms import ComplaintCreateForm

class ComplaintListView(ListView):
    model = Complaint


class ComplaintDetailView(DetailView):
    model = Complaint


class ComplaintCreateView(SuccessMessageMixin, CreateView):
    model = Complaint
    form_class = ComplaintCreateForm
    success_message = "%(name)s your complaint was created successfully"