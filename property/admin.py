from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('who_liked',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'address')

admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
