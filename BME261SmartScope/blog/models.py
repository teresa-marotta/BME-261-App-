from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

class Patient(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	info = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)
	technician = models.ForeignKey(User, on_delete=models.CASCADE)
	audio = models.FileField(upload_to='audio_files', null=True, verbose_name="")

	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse('patient-detail', kwargs={'pk': self.pk})




