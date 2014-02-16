from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from catalog.models import *
from django_summernote.admin import SummernoteModelAdmin

class AdvertismentAdmin(admin.ModelAdmin):
	pass
class InfoValueAdmin(admin.TabularInline):
    model = InfoValue

class ItemAdmin(admin.ModelAdmin):
    inlines = [InfoValueAdmin]


#admin.site.register(City, AdvertismentAdmin)
#admin.site.register(Category, MPTTModelAdmin)
#admin.site.register(CategoryField, AdvertismentAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, AdvertismentAdmin)
admin.site.register(InfoCategory, AdvertismentAdmin)
admin.site.register(InfoValue, AdvertismentAdmin)
#admin.site.register(AdvertismentImage, AdvertismentAdmin)

#admin.site.register(AdvertismentFieldValues,AdvertismentAdmin)
#admin.sites.register(
#admin.sites.register(
#admin.sites.register(

