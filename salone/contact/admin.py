from django.contrib import admin
from .models import Contact, Appointment

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
    search_fields = ("name", "email")
    list_filter = ("message",)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "date", "professional", "message")
    search_fields = ("name", "email", "phone", "date", "professional")
    list_filter = ("message",)
    