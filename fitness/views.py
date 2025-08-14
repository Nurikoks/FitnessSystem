from django.shortcuts import render
from rest_framework import viewsets
from .models import Trainer, Gym, Schedule, TrainersGym
from .serializers import TrainerSerializer, GymSerializer, ScheduleSerializer, TrainersGymSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class TrainersGymViewSet(viewsets.ModelViewSet):
    queryset = TrainersGym.objects.all()
    serializer_class = TrainersGymSerializer

