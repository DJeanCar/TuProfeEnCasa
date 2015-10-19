from django.shortcuts import render
from django.views.generic import CreateView

from .forms import TeacherForm

# Create your views here.
class WorkWithUsView(CreateView):

	form_class = TeacherForm
	template_name = 'main/connosotros.html'

	def form_valid(self, form):
		form.save()
		return render(self.request, 'main/connosotros.html', 
            {'message': 'Tus datos han sido enviados', 'form': TeacherForm()})