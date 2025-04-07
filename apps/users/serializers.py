from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User # опять точка и если убрать будет бабах


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']      # Я КАК ПОНЯЛ ТУТ СБОР ДАННЫХ ПОЛЬЗОВАТЕЛЯ И ОТПРАВКА В ВИДЕ ПЕРЕМЕННОЙ
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")     # а тут видимо проверка данных и возврат
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']