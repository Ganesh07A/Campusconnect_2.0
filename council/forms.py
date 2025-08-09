from django import forms
from .models import Council

class CouncilForm(forms.ModelForm):
    class Meta:
        model = Council
        fields = '__all__'
