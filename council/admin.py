from django.contrib import admin
from .models import Council

@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_post', 'contact')
