from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import PatientForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def PatientList(request):
	context = {
		'patients': Patient.objects.all()
	}
	return render(request, 'blog/patient_list.html', context)

class PatientListView(ListView):
	model = Patient
	template_name = 'blog/patient_list.html' 
	context_object_name = 'patients'
	ordering = ['-date_added']
	paginate_by = 5 

#To see all posts by specified user#
class UserPatientListView(ListView):
	model = Patient
	template_name = 'blog/user_patients.html' 
	context_object_name = 'patients'
	paginate_by = 5 

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Patient.objects.filter(technician=user).order_by('-date_added')

class PatientDetailView(DetailView):
	model = Patient

@login_required
def PatientCreate(request):
	if request.method == 'POST':
		form = PatientForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			messages.success(request, f'Your patient has been created!')
			return redirect('login')
	else:
		form = PatientForm()
	return render(request, 'blog/patient_form.html', {'form': form})

class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Patient
	fields = ['first_name', 'last_name', 'info', 'audio']

	def form_valid(self, form):
		form.instance.technician = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == patient.technician: 
			return True
		return False 

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Patient
	success_url = '/'

	def test_func(self):
		patient = self.get_object()
		if self.request.user == patient.technician: 
			return True
		return False 

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def home(request):
	return render(request, 'blog/home.html', {'title': 'Home'})

