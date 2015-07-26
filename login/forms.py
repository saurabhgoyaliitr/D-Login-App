
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from login.models import ProfileData


class ProfileForm(ModelForm):
	class Meta:
		model=ProfileData
		fields=('branch','enrollment','gender','dob','contact','address','about')
		widgets={'gender':forms.RadioSelect(),'dob':SelectDateWidget(years=range(1980,2000)),'about':forms.Textarea}



class PhotoUploadForm(forms.Form):
	profile = forms.ImageField()
