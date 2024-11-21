from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Project,Client,Employee,Department
from .serializers import Project_serializer,Client_serializer,Employee_serializer,Department_serializer
from datetime import date
# Create your views here.


@api_view(['GET'])
def check(request):
    s_date = date(2024,11,12)
    data = Project.objects.filter(start_date__lt=s_date) # for exact date use = ,for before __lt, for after __gt , on and before __lte similarly __gte for month start_date__month=11, for year start_date__year=2023
    serializer = Project_serializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def project_type(request):
    data = [i[1] for i in Project.project_type_choices]
    return Response(data,status=status.HTTP_200_OK)

@api_view(['GET'])
def status_name(request,name):
    data = Project.project_status_choices.get(name,[])
    f = [i[1] for i in data]
    return Response(f,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_client_name(request):
    data = Client.objects.all()
    serializer=Client_serializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_department_name(request):
    data = Department.objects.all()
    serializer=Department_serializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_Employee_data(request):
    data = Employee.objects.all()
    serializer=Employee_serializer(data,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def add_Project(request):
    print(request.data)
    serializer = Project_serializer(data=request.data)
    if serializer.is_valid():
        print('data is valid')
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        print('data invalid')
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)