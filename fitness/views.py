from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Trainer, Gym, Schedule, TrainersGym, Booking
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from .serializers import (
    TrainerSerializer,
    GymSerializer,
    ScheduleSerializer,
    TrainersGymSerializer,
    BookingSerializer
)
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [AllowAny]

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = [AllowAny]

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [AllowAny]

class TrainersGymViewSet(viewsets.ModelViewSet):
    queryset = TrainersGym.objects.all()
    serializer_class = TrainersGymSerializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer