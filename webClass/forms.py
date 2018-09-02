from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=200)
    desc = forms.CharField(max_length=30)

class DeleteForm(forms.Form):
    name = forms.CharField(max_length=200)

class SetDescForm(forms.Form):
    name = forms.CharField(max_length=200)
    desc = forms.CharField(max_length=30)

class SetIdForm(forms.Form):
    name = forms.CharField(max_length=200)
    id = forms.CharField(max_length=200)

class ArchiveForm(forms.Form):
    id = forms.CharField(max_length=200)

class LightsForm(forms.Form):
    frame = forms.CharField(max_length=3) #k
    rgb = forms.CharField(max_length=11) #r, g, b
    transition = forms.CharField(max_length=4)#m 1 for none m2 for fade
    time = forms.CharField(max_length=5)#time in ms max 99999
