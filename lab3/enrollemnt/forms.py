from django import forms
from .models import Student, Course


class EnrollForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(), empty_label="Select Student"
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), empty_label="Select Course"
    )
