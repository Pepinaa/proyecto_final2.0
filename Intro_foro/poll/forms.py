from django import forms
from .models import Poll

class CreatePollForm(forms.ModelForm):
    option_one = forms.CharField(max_length=30, initial="Sí", required=False)
    option_two = forms.CharField(max_length=30, initial="No", required=False)

    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two']

    def clean_option_one(self):
        return "Sí"

    def clean_option_two(self):
        return "No"