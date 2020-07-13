from django import forms
from .models import Investor


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = [
            'name',
            'about',
            'startups_funded',
            'contact',
            'email',
            'photo',
        ]    