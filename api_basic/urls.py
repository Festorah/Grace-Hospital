from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_basic import views

urlpatterns = [
    path('patients/', views.PatientList.as_view()),
    path('patients/<int:pk>/', views.PatientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)