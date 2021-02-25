from django.db import models


class DrugRequest(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=200)
	verification_number = models.CharField(max_length=200)
	

	def __str__(self):
		return self.name
