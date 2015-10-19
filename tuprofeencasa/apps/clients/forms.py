#encoding=utf-8
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

	class Meta:
		model = Client
		exclude = ('contacted',)
		widgets = {
			'full_name' : forms.TextInput(attrs={
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Nombres y Apellidos'
				}),
			'email' : forms.TextInput(attrs={
					'type' : 'email',
					'class' : 'form-control',
					'placeholder' : 'Email'
				}),
			'phone' : forms.TextInput(attrs={
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Teléfono'
				}),
			'message' : forms.Textarea(attrs={
					'class' : 'form-control',
					'placeholder' : 'Mensaje',
					'style' : 'height: 208px'
				})
		}