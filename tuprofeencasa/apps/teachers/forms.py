#encoding=utf-8
from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):

	class Meta:
		model = Teacher
		exclude = ('contacted',)
		widgets = {
			'first_name' : forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Nombres*',
					'required':'True',
				}),
			'last_name' : forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Apellidos*',
					'required':'True',
				}),
			'dni' : forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'DNI*',
					'required':'True',
				}),
			'age' : forms.TextInput(attrs = {
					'type' : 'number',
					'class' : 'form-control',
					'placeholder' : 'Edad*',
					'required':'True',
				}),
			'occupation' : forms.Select(attrs = {
					'class' : 'form-control',
					'required':'True',
					'style': 'margin-bottom: 15px'
				}),
			'disponibilidad_horaria' : forms.Textarea(attrs={
					'class' : 'form-control',
					'style' : 'height: 57px;margin-bottom: 15px',
					'required':'True',
					'placeholder' : 'Coméntanos sobre tu disponibilidad horaria'
				}),
			'trabajar_con_nosotros' : forms.Textarea(attrs={
					'required':'True',
					'class' : 'form-control',
					'style' : 'height: 57px;margin-bottom: 15px',
					'placeholder' : 'Cuéntanos porque te gustaría trabajar con nosotros'
				}),
			'cv' : forms.FileInput(attrs={
					'class' : 'form-control',
					'required':'True',
				})
		}





