from django.urls import path
from .views import PatientListView, PatientDetailView, PatientUpdateView, PatientDeleteView, UserPatientListView, PatientCreate
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('patientlist/', PatientListView.as_view(), name='patient-list'),
    path('user/<str:username>', UserPatientListView.as_view(), name='user-patients'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/new/', PatientCreate, name='patient-create'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    path('about/', views.about, name='blog-about'), 
]
