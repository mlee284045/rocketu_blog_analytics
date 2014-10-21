from django.contrib import admin
from analytics.models import Page, Location, View


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass