from django.contrib import admin
from .models import Profile

admin.site.site_header = 'State Hospital Asubiaro, Osogbo, Dashboard'

admin.site.register(Profile)
