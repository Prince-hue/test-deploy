from django import forms
from .models import deploy

class deployforms(forms.ModelForm):
    class Meta:
        model = deploy
        fields = ['name_of_websites']
        