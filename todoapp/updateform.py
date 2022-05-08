from django import forms
from .models import todomodel
from django.forms import ModelForm

class updform(ModelForm):
    class Meta:
        model = todomodel
        fields = ('work','time','date')