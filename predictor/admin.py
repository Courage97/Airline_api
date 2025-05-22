from django.contrib import admin
from .models import PredictionLog


@admin.register(PredictionLog)
class PredictionLogAdmin(admin.ModelAdmin):
    list_display = (
        'prediction',
        'confidence',
        'seat_number',
        'location',
        'flight_date',
        'flight_number',
        'timestamp',
    )
    list_filter = ('prediction', 'location', 'flight_date')
    search_fields = ('seat_number', 'location', 'flight_number')
    ordering = ('-timestamp',)
    readonly_fields = ('input_data', 'prediction', 'confidence', 'timestamp')
