from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class imageSerializer(serializers.ModelSerializer):


    class Meta:
        model = image
        fields = '__all__'
        depth = 1


class nameSerializer(serializers.ModelSerializer):

    class Meta:
        model = name
        fields = '__all__'
        depth = 1

class cls_typeSerializer(serializers.ModelSerializer):


    class Meta:
        model = cls_type
        fields = '__all__'
        depth = 1


class studentSerializer(serializers.ModelSerializer):
    # name = nameSerializer(many=True)

    class Meta:
        model = student
        fields = '__all__'

class studentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class userCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = manager
        fields = ['username', 'password', 'cls']

    def create(self, validated_data):
        user = manager.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.is_active = True
        user.save()

        return user