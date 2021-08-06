from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from patients.models import Patient
from api_basic.serializers import PatientSerializer



class PatientList(APIView):

	def get(self, request, format=None):
		patients = Patient.objects.all()
		serializer = PatientSerializer(patients, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PatientSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)




class PatientDetail(APIView):

	def get_object(self, pk):
		try:
			patient = Patient.objects.get(pk=pk)
		except Patient.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		patient = self.get_object(pk)
		serializer = PatientSerializer(patient)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		patient = self.get_object(pk)
		serializer = PatientSerializer(patient, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		patient = self.get_object(pk)
		patient.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




# This is for Function base views


# @api_view(['GET', 'POST'])
# def patient_list(request, format=None):
# 	if request.method == 'GET':
# 		patients = Patient.objects.all()
# 		serializer = PatientSerializer(patients, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = PatientSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def patient_detail(request, pk, format=None):
# 	try:
# 		patient = Patient.objects.get(pk=pk)
# 	except Patient.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = PatientSerializer(patient)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = PatientSerializer(patient, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		patient.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)