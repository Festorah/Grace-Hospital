from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('check_test_result/', views.check_result, name='check-test-result'),
	path('my_result/', views.my_result, name='my-result'),
	path('staff_blog/', views.staff_blog, name='staff-blog'),
	path('my_drug/', views.my_drug, name='my-drug'),
	path('render_pdf_view/<int:pk>/', views.render_pdf_view, name='render-pdf-view'),
	path('get_drugs/', views.get_drugs, name='get-drugs'),
	path('instructional_materials', views.instructional_materials, name='instructional-materials'),
]