from django.contrib import admin
from .models import Car, Make, Model, Category, Reservation

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'make', 'model', 'model_date', 'seats', 'color', 'price')
    list_filter = ('category', 'make', 'model')
    search_fields = ('make__name', 'model__name', 'category__name', 'color')
    list_per_page = 20

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'pickup_location', 'drop_off_location', 'reservation_date', 'reservation_time', 'passengers')
    list_filter = ('reservation_date', 'pickup_location', 'drop_off_location')
    search_fields = ('user__username', 'pickup_location__name', 'drop_off_location__name')

admin.site.register(Car, CarAdmin)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Category)