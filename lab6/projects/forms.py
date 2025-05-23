from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["student", "topic", "languages_used", "duration_weeks"]
