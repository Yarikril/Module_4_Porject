from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_date","updated_date","auction"]
    list_filter = ['auction', "created_at"]
    actions = ["diseable_auction", "enable_auction"]

    @admin.action(description="убрать возможность торга")
    def diseable_auction(self,request,queryset):
        queryset.update(auction = False)

    @admin.action(description="добавить возможность торга")
    def enable_auction(self,request,queryset):
        queryset.update(auction = True)

    fieldsets = (
    ("Обшие",{"fields":("title","description")}),
    ("Финансы",{"fields":("price", "auction"), "classes": ['collapse']})
    )
admin.site.register(Advertisement, AdvertisementAdmin)