from django.contrib import admin
from data.models import *

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_filter = ('condition','serialnumber',)
    list_display = ('item_detail','serialnumber','vendor',)
    


admin.site.register(Items, ItemsAdmin)
admin.site.register(Condition)
admin.site.register(Vendor)
admin.site.register(Location)
admin.site.register(ItemDetail)
admin.site.register(Technical)

