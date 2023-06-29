from django.contrib import admin

from .models import Complaint, ComplaintHandling

admin.site.register(Complaint)
admin.site.register(ComplaintHandling)
