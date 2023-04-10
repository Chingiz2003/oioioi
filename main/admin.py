from django.contrib import admin

# Register your models here.

from .models import Ads, Category, Mark, MarkModel, Engine, Rudder


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'marks', 'created_ad', 'updated_ad', 'is_published')
    list_display_links = ('id', 'marks')
    search_fields = ('marks', 'full_text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class MarkModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'name')
    list_display_links = ('id', 'mark')
    search_fields = ('mark', 'name')

class EngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class RudderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Engine, EngineAdmin)

admin.site.register(Rudder, RudderAdmin)

admin.site.register(MarkModel, MarkModelAdmin)

admin.site.register(Mark, MarkAdmin)

admin.site.register(Ads, AdsAdmin)

admin.site.register(Category, CategoryAdmin)