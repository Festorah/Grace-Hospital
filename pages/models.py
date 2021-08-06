from django.db import models


class DrugRequest(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=200)
	verification_number = models.CharField(max_length=200)
	

	def __str__(self):
		return self.name


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	message = models.TextField(default='Message...', blank=True, null=True)
	

	def __str__(self):
		return self.name

class Newsletter(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email