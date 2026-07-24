from django import forms
from .models import StudioBooking, BeatPurchase

class StudioBookingForm(forms.ModelForm):
    class Meta:
        model = StudioBooking
        fields = [
            'full_name',
            'phone',
            'email',
            'service',
            'preferred_date',
            'preferred_time',
            'project_title',
            'message',
            'proof_of_payment',
        ]
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })


class BeatPurchaseForm(forms.ModelForm):
    class Meta:
        model = BeatPurchase
        fields = [
            'full_name',
            'phone',
            'email',
            'beat',
            'proof_of_payment',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'required': 'required'
            })