from django import forms

from .models import Complaint, ComplaintHandling


class ComplaintCreateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"
        widgets = {
            "complaint": forms.Textarea(
                attrs={"rows": 20},
            ),
            "summary": forms.Textarea(
                attrs={"rows": 3},
            ),
            "date_purchased": forms.TextInput(attrs={"type": "date"}),
            "manufactured_date": forms.TextInput(attrs={"type": "date"}),
        }
        # labels = {
        #     "carer": "",
        # }
