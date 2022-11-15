from django.urls import path, include
from .views import students_list
urlpatterns = [
    path('users', students_list)
]
