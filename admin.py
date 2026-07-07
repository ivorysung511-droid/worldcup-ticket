from django.contrib import admin
from .models import Event, Venue

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'venue', 'city', 'min_price', 'tickets_available']
    list_filter = ['stage', 'city', 'is_active']
    search_fields = ['title', 'venue', 'team1', 'team2']
    ordering = ['date']

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'country', 'capacity']
    search_fields = ['name', 'city']
