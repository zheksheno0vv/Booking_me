from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *



class HotelPhotosInline(admin.TabularInline):
    model = HotelPhotos
    extra = 1


class HotelPhotoLanguagesAdmin(admin.ModelAdmin):
    inlines = [HotelPhotosInline]


class RoomPhotosInline(admin.TabularInline):
    model = RoomPhotos
    extra = 1

class RoomPhotosLanguagesAdmin(admin.ModelAdmin):
    inlines = [RoomPhotosInline]


@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelPhotosInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomPhotosInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Booking)



