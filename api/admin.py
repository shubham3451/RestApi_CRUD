from django.contrib import admin
from .models import data

# Register your models here.
@admin.register(data)
class dataAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll', 'city']