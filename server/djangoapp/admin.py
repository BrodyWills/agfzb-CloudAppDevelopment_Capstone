from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel


# Register your models here.

class CarModelInLine(admin.StackedInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    fields = ['make', 'name', 'dealerId', 'carType', 'year']

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInLine]
    fields = ['name', 'description']

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)