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


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def cluster_list(request):
    if request.method == 'GET':
        # data = User.objects.all()
        # serializer = WablasSerializers(
        #     data, context={'request': request}, many=True)
        return Response("Data")
    elif request.method == 'POST':
        # POST DATA CLUSTER
        upload = request.FILES['file']
        excel_data_df = pandas.read_excel(upload)
        thisisjson = excel_data_df.to_json(orient='records')
        return Response({'data': json.dumps(thisisjson)})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def broadcast_list(request):
    if request.method == 'GET':
        return Response("Data")
        # POST DATA BROACAST SEND ONE
    elif request.method == 'POST':
        nama = request.data['nama']
        number = request.data['number']
        segmen = request.data['segmen']
        return Response(request.data)
        # POST DATA BROACAST SEND > ONE
    elif request.method == 'PUT':
        nama = request.data['nama']
        number = request.data['number']
        segmen = request.data['segmen']
        return Response(request.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def wa_blast(request):
    if request.method == 'GET':
        return Response("Data")
        # POST DATA CLUSTER SEND ONE PERSON
    elif request.method == 'POST':
        nama = request.data['nama']
        number = request.data['number']
        segmen = request.data['segmen']
        return Response()
        # POST DATA CLUSTER SEND  > ONE PERSON
    elif request.method == 'PUT':
        nama = request.data['nama']
        number = request.data['number']
        segmen = request.data['segmen']
        return Response([segmen, nama])
