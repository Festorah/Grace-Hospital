from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
	list_display = ('name', 'test_result', 'date_tested', 'extra_field')
	list_filter = ('test_result', 'date_tested', 'gender', 'officer_in_charge')


admin.site.register(Patient, PatientAdmin)