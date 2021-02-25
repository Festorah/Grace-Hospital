from django.urls import path
from .views import (PatientListView,
	PatientDetailView,
	PatientUpdateView,
	PatientCreateView,
	UserPatientListView,
	PatientDeleteView
)
from . import views

urlpatterns = [
	path('', PatientListView.as_view(), name='patients-home'),
	path('user/<str:username>', UserPatientListView.as_view(), name='user-patients'),
	path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
	path('patient/new/', PatientCreateView.as_view(), name='patient-create'),
	path('patient/<int:pk>/update', PatientUpdateView.as_view(), name='patient-update'),
	path('patient/<int:pk>/delete', PatientDeleteView.as_view(), name='patient-delete'),
	path('search/', views.search, name='search'),
	
]


