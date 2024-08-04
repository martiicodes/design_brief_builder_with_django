from django import forms
from .models import DesignBrief

class DesignBriefForm(forms.ModelForm):
    class Meta:
        model = DesignBrief
        fields = [
            'client_name',
            'project_name',
            'email',
            'project_description',
            'objectives',
            'target_audience',
            'competitors',
            'deliverables',
            'budget',
            'deadline',
        ]