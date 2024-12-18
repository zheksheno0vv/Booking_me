from .models import Hotel
from django_filters import FilterSet

class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {

          'created_date': ['gt', 'lt'],

        }