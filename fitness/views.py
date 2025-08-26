from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Trainer, Gym, Schedule, TrainersGym, Booking
from .serializers import (
    TrainerSerializer,
    GymSerializer,
    ScheduleSerializer,
    TrainersGymSerializer,
    BookingSerializer
)

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
