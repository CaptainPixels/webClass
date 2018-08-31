from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=200)

class SetIdForm(forms.Form):
    name = forms.CharField(max_length=200)
    id = forms.CharField(max_length=200)

class ArchiveForm(forms.Form):
    id = forms.CharField(max_length=200)
