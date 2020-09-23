from django.forms import ModelForm
from Tollywood.models import *

class HeroForm(ModelForm):
	class Meta:
		model=Heroregister
		fields='__all__'

class HeroForm2(ModelForm):
	class Meta:
		model=Heroregister
		fields=['heroage','herofilmcount']

class ContactForm(ModelForm):
	class Meta:
		model=Contact
		fields='__all__'

