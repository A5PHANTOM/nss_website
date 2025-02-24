from django import forms
from .models import Program, ProgramPhoto, MoreProgramPhoto

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description', 'poster_image', 'more_description']


class ProgramPhotoForm(forms.ModelForm):
    class Meta:
        model = ProgramPhoto
        fields = ['image']


class MoreProgramPhotoForm(forms.ModelForm):
    class Meta:
        model = MoreProgramPhoto
        fields = ['image']
