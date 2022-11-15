from django.db import models
from rest_framework import serializers
# Create your models here.


class User(models.Model):
    id = serializers.IntegerField(read_only=True)
    name = models.CharField(blank=True, max_length=50, default='users')
    slug = models.CharField(blank=True, max_length=50, unique=True)
    emails = models.CharField(
        blank=True, max_length=50, default='users@gmail.com')
    password = models.CharField(
        blank=True, max_length=100, default='users')
    created = models.DateTimeField(auto_now_add=True)


class Wablas(models.Model):
    id = serializers.IntegerField(read_only=True)
    name = models.CharField(blank=True, max_length=50, default='users')
    slug = models.CharField(blank=True, max_length=50, unique=True)
    file = models.CharField(
        blank=True, max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
