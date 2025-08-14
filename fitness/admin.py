from django.contrib import admin

from .models import Gym, User, Trainer, Schedule, Booking, TrainersGym

admin.site.register(Gym)
admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Schedule)
admin.site.register(Booking)
admin.site.register(TrainersGym)
