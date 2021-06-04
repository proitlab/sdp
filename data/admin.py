from django.contrib import admin
from data.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ConditionResource(resources.ModelResource):
    class Meta:
        model = Condition
        exclude = ('created_at', 'updated_at', )

class StatusResource(resources.ModelResource):
    class Meta:
        model = Status
        exclude = ('created_at', 'updated_at', )

class VendorResource(resources.ModelResource):
    class Meta:
        model = Vendor
        exclude = ('created_at', 'updated_at', )

class TechnicalResource(resources.ModelResource):
    class Meta:
        model = Technical
        exclude = ('created_at', 'updated_at', )

class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        exclude = ('created_at', 'updated_at', )

class ItemDetailResource(resources.ModelResource):
    class Meta:
        model = ItemDetail
        exclude = ('created_at', 'updated_at', )

class ItemsResource(resources.ModelResource):
    class Meta:
        model = Items
        exclude = ('created_at', 'updated_at', )


class ItemDetailAdmin(ImportExportModelAdmin):
    resource_class = ItemDetailResource


class LocationAdmin(ImportExportModelAdmin):
    resource_class = LocationResource

class TechnicalAdmin(ImportExportModelAdmin):
    resource_class = TechnicalResource

class VendorAdmin(ImportExportModelAdmin):
    resource_class = VendorResource

class ConditionAdmin(ImportExportModelAdmin):
    resource_class = ConditionResource

class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource


class ItemsAdmin(ImportExportModelAdmin):
    resource_class = ItemsResource
    list_filter = ('serialnumber',)
    list_display = ('serialnumber', 'item_name', 'status', 'condition', 'location', 'date_out', 'date_in')
    search_fields = ['item_detail', 'serialnumber', 'location',]

    fieldsets = (
            ('SN, Name and Vendor ', {
                'classes': ('collapse',),
                'fields' : (
                    'serialnumber',
                    'item_name',
                    'vendor',
                    )
                }),
            ('LTCS', {
                'classes': ('collapse',),
                'fields' : (
                    'location',
                    'technical',
                    'condition',
                    'status',
                )
                }),
            ('Accept', {
                'classes': ('collapse',),
                'fields' : (
                    'date_accept',
                    'reason_accept',
                )
                }),
            ('Out', {
                'classes': ('collapse',),
                'fields' : (
                    'date_out',
                    'reason_out',
                )
                }),
            ('In', {
                'classes': ('collapse',),
                'fields': (
                    'date_in',
                    'reason_in',
                )
                }),
        )

    
admin.site.register(Items, ItemsAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ItemDetail, ItemDetailAdmin)
admin.site.register(Technical, TechnicalAdmin)

