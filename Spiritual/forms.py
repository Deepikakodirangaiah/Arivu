from django import forms
from .models import SpiritualTalk

class SpiritualTalkForm(forms.ModelForm):
    class Meta:
        model = SpiritualTalk
        fields = ['title', 'speaker', 'date', 'description', 'video_url']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }