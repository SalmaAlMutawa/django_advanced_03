from django.contrib import admin
from .models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'description',]
	list_filter = ['name', 'description', ]
	list_filter = ['added',]
	list_editable = ['description', ]

admin.site.register(Store, StoreAdmin)