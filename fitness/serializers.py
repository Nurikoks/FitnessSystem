from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Trainer, Gym, Schedule, TrainersGym, Booking

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class TrainersGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainersGym
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user