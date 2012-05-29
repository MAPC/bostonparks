from django import forms
from models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ('park',)
        widgets = dict(rating=forms.RadioSelect())