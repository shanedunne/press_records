from django.contrib import admin
from .models import JoinMailList

class JoinMailListAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'timestamp',
    )

admin.site.register(JoinMailList, JoinMailListAdmin)
