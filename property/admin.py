from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInLine(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)
    fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('who_liked',)
    inlines = [OwnerInLine,]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'address')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'owners_phonenumber', 'owner_pure_phone')
    raw_id_fields = ('flats', )


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
