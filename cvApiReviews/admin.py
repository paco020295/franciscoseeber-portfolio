from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    fields = ['id', 'title', 'client_name', 'client_city', 'client_latitude', 'client_longitude', 'average_score', 'skills', 'quality', 'availability', 'deadlines', 'communication', 'cooperation', 'start_date', 'end_date', 'review_text', 'client_country']
    list_display = ['id', 'title', 'client_name', 'client_country']


admin.site.register(Review, ReviewAdmin)
