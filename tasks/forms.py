from django import forms
from django.forms import ModelForm

from .models import *


class Taskform(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'complete',]
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.fields['title'].label='title'

