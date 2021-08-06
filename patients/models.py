from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


NEGATIVE = 'Negative'
AWAITING = 'Awaiting'
POSITIVE = 'Positive'
CHOICE = (
	(NEGATIVE, 'Negative'), 
	(POSITIVE, 'Positive'), 
	(AWAITING, 'Awaiting'),
	)

MALE = 'Male'
FEMALE = 'Female'
GENDER = (
	(MALE, 'Male'), 
	(FEMALE, 'Female'),
	)

class Patient(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	age = models.IntegerField()
	address = models.CharField(max_length=200)
	test_result = models.CharField(choices=CHOICE, default=AWAITING, max_length=100)
	gender = models.CharField(choices=GENDER, default=MALE, max_length=100)
	officer_in_charge = models.ForeignKey(User, on_delete=models.CASCADE)
	date_tested = models.DateTimeField(default=timezone.now)
	verification = models.CharField(max_length=200, blank=False, default='osun')
	phone_number = models.BigIntegerField(default=2347000000, blank=True)

	extra_field = models.CharField(choices=CHOICE, default=AWAITING, max_length=100)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('patient-detail', kwargs={'pk':self.pk})

	def save(self, commit=True):
		extra_field = self.cleaned_data.get('extra_field', None)
		# ...do something with extra_field here...
		return super(Patient, self).save(commit=commit)

