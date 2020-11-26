
from django import forms  
from .models import *

class BannerForm(forms.ModelForm): 
  
    class Meta: 
        model = Banner 
        fields = ['name', 'banner_image']

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description','attach_file']

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['title','programme_mission', 'description','incharge_teacher','programme_image']
class admin_regestion_meForm(forms.ModelForm):
	class Meta:
		model=admin_regestion_me
		fields="__all__"