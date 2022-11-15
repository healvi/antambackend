from email import message
from unicodedata import name
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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")


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
        df = pandas.read_excel(("."+file_url), header=0)
        
        # os.system("")
        # os.environ["WDM_LOG_LEVEL"] = "0"
        
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--profile-directory=Default")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        delay = 30
        driver.get('https://web.whatsapp.com')
        
        name_phone_dict = dict(zip(df['nama'].tolist(), df['no_telp'].tolist()))
        for _, (name, phone) in enumerate(name_phone_dict.items()):
            try:
                message = "Hi" + " " + name
                phone = "+" + str(phone)
                url = 'https://web.whatsapp.com/send?phone=' + str(phone) + '&text=' + message
                sent = False
                for i in range(3):
                    if not sent:
                        driver.get(url)
                        try:
                            click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                        except Exception as e:
                            print(f"\nFailed to send message to: {str(phone)}, retry ({i+1}/3)")
                            print("Make sure your phone and computer is connected to the internet.")
                            print("If there is an alert, please dismiss it.")
                        else:
                            sleep(1)
                            click_btn.click()
                            sent=True
                            sleep(3)
            except Exception as e:
                print('Failed to send message to ' + str(phone) + str(e))
            # print(k, v)
        driver.close()
                
        res = df.to_json(orient="columns")
        # parsed = json.loads(res)
        parsed = json.dumps(res)
        return Response({'response': json.dumps(parsed)}, content_type="application/json")


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
