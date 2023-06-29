from django.db import models
from django.urls import reverse

MALE = "MALE"
FEMALE = "FEMALE"
RATHER_NOT_SAY = "RATHER_NOT_SAY"
GENDER_CHOICES = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (RATHER_NOT_SAY, "RATHER NOT SAY"),
)

AGE_13_17 = "13 - 17"
AGE_18_25 = "18 - 25"
AGE_26_35 = "26 - 35"
AGE_36_50 = "36 - 50"
AGE_OVER_50 = "OVER 50"

AGE_GROUP_CHOICES = (
    (AGE_13_17, "13 - 17"),
    (AGE_18_25, "18 - 25"),
    (AGE_26_35, "26 - 35"),
    (AGE_36_50, "36 - 50"),
    (AGE_OVER_50, "over 50"),
)

REFUND = "REFUND"
EXCHANGE = "EXCHANGE"
REPAIR = "REPAIR"
CREDIT_NOTE = "CN"
OTHER = "OTHER"

REDRESS_CHOICES = (
    (REFUND, "REFUND"),
    (EXCHANGE, "EXCHANGE"),
    (REPAIR, "REPAIR"),
    (CREDIT_NOTE, "CREDIT NOTE"),
    (OTHER, "OTHER"),
)


class Complaint(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(max_length=100, blank=True)
    id_number = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=11)
    phone1 = models.CharField(max_length=11, blank=True)
    gender = models.CharField(
        max_length=15, choices=GENDER_CHOICES, default=RATHER_NOT_SAY
    )
    age_group = models.CharField(
        max_length=7, choices=AGE_GROUP_CHOICES, default=AGE_OVER_50
    )
    business_name = models.CharField(max_length=255)
    business_address = models.CharField(max_length=255, blank=True)
    business_sector = models.CharField(max_length=255, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    business_phone = models.CharField(max_length=11, blank=True)
    business_email = models.EmailField(blank=True)
    goods_services = models.CharField("Goods/Services", max_length=255, blank=True)
    model_serial_number = models.CharField("Model/Serial number", max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    date_purchased = models.DateField(blank=True, null=True)
    warranty_guaranty = models.CharField("warranty/Guaranty",max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    brand_code = models.CharField(max_length=255, blank=True)
    invoice_receipt_bill = models.CharField("Invoice/Receipt/Bill",max_length=255, blank=True)
    manufactured_date = models.DateField(blank=True, null=True)
    standard = models.CharField(max_length=255, blank=True)
    electrical_frequency_rating = models.CharField(max_length=255, blank=True)
    voltage_required = models.CharField(max_length=255, blank=True)
    complaint = models.TextField()
    redress = models.CharField(max_length=10, choices=REDRESS_CHOICES, default=REFUND,help_text='if other please state redress')
    other_redress = models.CharField(max_length=255, blank=True)
    i_agree = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("complaint-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}, {self.summary}"


class ComplaintHandling(models.Model):
    complaint = models.ForeignKey(
        Complaint, on_delete=models.PROTECT, related_name="handling"
    )
    officer = models.CharField(max_length=255, blank=True, null=True)
    investigating_officer = models.CharField(max_length=255, blank=True, null=True)
    ministry_liaison = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    exhibits = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("handling-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.complaint.name
