from rest_framework import serializers
from .models import User, Wablas


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'emails', 'name', 'slug', 'password', 'created')


class WablasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wablas
        fields = ('id', 'name', 'slug', 'file', 'created')
