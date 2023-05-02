from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.
# specify how you want the admin page to look like for flights
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger,PassengerAdmin)
