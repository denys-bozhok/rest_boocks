from django.contrib import admin
from .models import Boock


# Register your models here.
class BoockAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Boock, BoockAdmin)
