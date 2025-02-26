from django import forms
from .models import Program, ProgramPhoto, MoreProgramPhoto,UpcomingEvent

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

class UpcomingEventForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvent
        fields = ['title', 'date', 'description', 'link']