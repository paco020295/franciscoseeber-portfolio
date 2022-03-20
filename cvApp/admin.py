from django.contrib import admin
from .models import Competence


class CompetenceAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'logo']
    list_display = ['title']


admin.site.register(Competence, CompetenceAdmin)
