from django.contrib import admin
from .models import Parking, Reservation, Category, Profile


# Register your models here.
admin.site.register(Parking)
admin.site.register(Reservation)
admin.site.register(Category)
admin.site.register(Profile)