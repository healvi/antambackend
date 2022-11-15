from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from .models import User, Wablas
from .serializers import UserSerializers, WablasSerializers
# Create your views here.
import pandas
import json


@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = User.objects.all()

        serializer = WablasSerializers(
            data, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WablasSerializers(data=request.data)
        upload = request.FILES['file']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        excel_data_df = pandas.read_excel(upload)
        thisisjson = excel_data_df.to_json(orient='records')
        return Response({'file_url': thisisjson})


# @api_view(['PUT', 'DELETE'])
# def students_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
