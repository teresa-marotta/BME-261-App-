from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Patient

#def home(request):
#	context = {
#		'posts': Post.objects.all()
#	}
#	return render(request, 'blog/home.html', context)

def home(request):
	return render(request, 'blog/homet.html', {'title': 'About'})

class PatientListView(ListView):
	model = Patient
	template_name = 'blog/home.html' 
	context_object_name = 'patients'
	ordering = ['-date_posted']
	paginate_by = 5 

#To see all posts by specified user#
class UserPatientListView(ListView):
	model = Patient
	template_name = 'blog/user_posts.html' 
	context_object_name = 'patients'
	paginate_by = 5 

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Patient.objects.filter(author=user).order_by('-date_posted')

class PatientDetailView(DetailView):
	model = Patient

class PatientCreateView(LoginRequiredMixin, CreateView):
	model = Patient
	fields = ['first_name', 'last_name', 'info', 'audio']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Patient
	fields = ['first_name', 'last_name', 'info', 'audio']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == patient.author: 
			return True
		return False 

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Patient
	success_url = '/'

	def test_func(self):
		patient = self.get_object()
		if self.request.user == patient.author: 
			return True
		return False 

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



