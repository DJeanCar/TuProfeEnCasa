from django.shortcuts import render
from django.views.generic import FormView
from apps.clients.forms import ClientForm

class HomeView(FormView):

	form_class = ClientForm
	template_name = 'main/index.html'

	def form_valid(self, form):
		form.save()
		return render(self.request, 'main/index.html', 
            {'message': 'Tus datos han sido enviados', 'form': ClientForm()})