from django.contrib import admin
from .models import Advertisement
from django.utils.safestring import mark_safe

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_date","updated_date","auction",'display_image']
    list_filter = ['auction', "created_at"]
    actions = ["diseable_auction", "enable_auction"]

    @admin.action(description="убрать возможность торга")
    def diseable_auction(self,request,queryset):
        queryset.update(auction = False)

    @admin.action(description="добавить возможность торга")
    def enable_auction(self,request,queryset):
        queryset.update(auction = True)

    fieldsets = (
    ("Обшие",{"fields":("title","description",'image','display_image')}),
    ("Финансы",{"fields":("price", "auction"), "classes": ['collapse']})
    )

    readonly_fields = ["display_image"]

    @admin.display(empty_value="static\img\pict.png")
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')

admin.site.register(Advertisement, AdvertisementAdmin)