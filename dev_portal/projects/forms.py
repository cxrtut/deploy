from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'picture', 'description', 'url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }