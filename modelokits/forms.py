from django.forms import ModelForm
from .models import Kits
from django import forms

class KitsForm(ModelForm):
	class Meta:
		model = Kits
		fields = '__all__'
		labels = {
			'name': 'Nombre',
			'principal': 'Es un principal?',
			'minimun': 'Número de unidades mínimo en packing'
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'minimun': forms.NumberInput(attrs={'class': 'form-control'}),
		}