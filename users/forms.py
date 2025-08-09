# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    from django import forms

class StudentRegistrationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'  # Bootstrap input style

    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]

    full_name = forms.CharField(max_length=100, help_text='Enter your full name as per records.')
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), help_text='YYYY-MM-DD')
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        help_text='Select your academic year.',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    prn = forms.CharField(max_length=20, help_text='Your Permanent Registration Number')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'full_name', 'dob', 'year', 'prn')

    def clean_prn(self):
        prn = self.cleaned_data['prn']
        if Student.objects.filter(prn=prn).exists():
            raise forms.ValidationError("This PRN is already registered.")
        return prn

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and self.instance.pk is None and self._meta.model.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email