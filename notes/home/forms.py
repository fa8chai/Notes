from django.contrib.auth.forms import forms
from django.contrib.admin import widgets
from .models import Note
from string import Template
from django.utils.safestring import mark_safe



class NoteForm(forms.ModelForm):
      reminder = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}))
      class Meta:
            model = Note
            fields=['note','reminder']

      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['note'].widget.attrs.update({'class':('note'),'rows':4, 'placeholder':'Write a note...'})


class SearchForm(forms.Form):
      search_reminder = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type':'date'}))

