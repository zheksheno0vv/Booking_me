from .models import Hotel, Room, Review
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')

@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_name', 'description')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('description',)

