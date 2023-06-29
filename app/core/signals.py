from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ComplaintHandling, Complaint


@receiver(post_save, sender=Complaint)
def create_complaint_handler(sender, instance, created, **kwargs):
    if created:
        ComplaintHandling.objects.create(complaint=instance)


# @receiver(post_save, sender=Complaint)
# def save_complaint(sender, instance, **kwargs):
#     instance.complaint.save()