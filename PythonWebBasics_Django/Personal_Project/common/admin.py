from django.contrib import admin

# Register your models here.
from common.models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'day', 'time')
    list_filter = ('day', 'time')

admin.site.register(Booking, BookingAdmin)