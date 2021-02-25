from django.shortcuts import render
import os
from .models import Patient
from covid_response.settings import STATIC_ROOT
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.auth.decorators import login_required


class PatientListView(LoginRequiredMixin, ListView):
	# files = os.listdir(os.path.join(STATIC_ROOT, 'patients/home'))
	# for file in files:
	# 	image = file
	model = Patient
	template_name = 'patients/patients_list.html'
	context_object_name = 'patients'
	ordering = ['-date_tested']
	paginate_by = 5



class UserPatientListView(LoginRequiredMixin, ListView):
	model = Patient
	template_name = 'patients/user_patients.html'
	context_object_name = 'patients'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Patient.objects.filter(official_in_charge=user).order_by('-date_tested')


class PatientDetailView(LoginRequiredMixin, DetailView):
	model = Patient
	template_name = 'patients/patient_detail.html'

	def patient_detail(request):
		patient = Patient.objects.get(pk=pk)
		context = { 'patients': patient }
		return render(request, template_name, context)



class PatientCreateView(LoginRequiredMixin, CreateView):
	model = Patient
	fields = ['name', 'email', 'gender', 'age', 'address', 'test_result', 'phone_number']

	def form_valid(self, form):
		verify_number1 = 0
		verify_number = Patient.objects.count()
		verify_number1 += verify_number
		new_verify = 'osun/covid/000'+ str(verify_number1)
		print(verify_number, verify_number1, new_verify)
		form.instance.officer_in_charge = self.request.user
		form.instance.verification = new_verify
		return super().form_valid(form)



class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	template_name = 'patients/patient_update.html'
	model = Patient
	fields = ['name', 'test_result']

	def form_valid(self, form):
		form.instance.official_in_charge = self.request.user
		return super().form_valid(form)

	def test_func(self):
		patient = self.get_object()
		if self.request.user == patient.officer_in_charge:
			return True
		print('oh me')
		return False


class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Patient
	success_url = '/patients/'

	def test_func(self):
		patient = self.get_object()
		if self.request.user == patient.officer_in_charge:
			return True
		return False

@login_required
def search(request):
	patients = Patient.objects.order_by('-date_tested')

	if 'address' in request.GET:
		address = request.GET['address']
		if address:
			patients = patients.filter(address__icontains=address)

	if 'name' in request.GET:
		name = request.GET['name']
		if name:
			patients = patients.filter(name__iexact=name)

	if 'test_result' in request.GET:
		test_result = request.GET['test_result']
		if test_result:
			patients = patients.filter(test_result__icontains=test_result)


	if 'age' in request.GET:
		age = request.GET['age']
		if age:
			patients = patients.filter(age__lte=age)

	context = {
		'patients': patients,
	}
	for patient in patients:
		print(patient.name)
	print('home')
	return render(request, 'patients/search.html', context)