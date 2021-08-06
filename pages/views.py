from django.shortcuts import render, redirect, get_object_or_404
from patients.models import Patient
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from .models import DrugRequest, Contact, Newsletter
from django.contrib.auth.decorators import login_required




def home(request):

	if request.method == 'POST':
		contact = Contact()
		newsletter = Newsletter()

		contact.name = request.POST.get('name')
		contact.email = request.POST.get('email')
		contact.subject = request.POST.get('subject')
		contact.message = request.POST.get('message')

		newsletter.email = request.POST.get('newsletter_email')

		if contact.name != None:
			contact.save()
			messages.success(request, 'Thank you for subscribing for our newsletter. You will hear from us soon.')

		if newsletter.email != None:
			newsletter.save()
		
			messages.success(request, 'Thank you for contacting us. You will hear from us soon.')

		return render(request, 'pages/home.html')

	return render(request, 'pages/home.html')

def check_result(request):
		return render(request, 'pages/check_test_result.html')

@login_required
def staff_blog(request):
	return render(request, 'pages/staff_blog.html')


def render_pdf_view(request, *args, **kwargs):
	pk = kwargs.get('pk')
	patient = get_object_or_404(Patient, pk=pk)

	template_path = 'pages/my_test_result_pdf.html'
	context = { 'patient': patient }
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="my_test_result.pdf"'
	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)
	# create a pdf
	pisa_status = pisa.CreatePDF(html, dest=response)
	# if error then show some funy view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response


def my_result(request):

	try:

		if request.method == 'POST':
			name = request.POST['name']
			verification_number_initial = request.POST['verification_number']
			email = request.POST['email']
			name2 = Patient.objects.filter(name=name).first()
			name2_id = name2.verification
			verification_number = str(name2_id)
			name3 = str(name2)
			print(type(verification_number_initial))
			print(type(verification_number))
			if name == name3 and verification_number_initial == verification_number:
				print('Yes', name, name2, name2_id)
				context = { 'name2': name2, 'name2_id': name2_id }
				return render(request, 'patients/test_result.html', context)
				
			else:
				print('Help')
				return render(request, 'pages/check_test_result.html')

		else:
			return render(request, 'pages/check_test_result.html')

	except ValueError:
		print('City or state missing')

	# patient = Patient.objects.get(pk=pk)
	# context = { 'patients': patients }



def get_drugs(request):
	return render(request, 'pages/get_drugs.html')

def my_drug(request):
	if request.method == 'POST':
		drug = DrugRequest()
		drug.name = request.POST['name']
		drug.verification_number = request.POST['verification_number']
		drug.email = request.POST['email']
		drug.phone_number = request.POST['phone_number']

		drug.save()
		
		messages.success(request, 'Your request has been made. Check your email for the venue')

		return render(request, 'pages/home.html')



def instructional_materials(request):
	return render(request, 'pages/instructional_materials.html')


