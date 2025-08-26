from rest_framework import routers
from .views import TrainerViewSet, GymViewSet, ScheduleViewSet, TrainersGymViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'trainers', TrainerViewSet)
router.register(r'gyms', GymViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'trainers-gyms', TrainersGymViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = router.urls