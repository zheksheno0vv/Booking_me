from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
               'phone_number',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class HotelPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = ['hotel_image']

class RatingSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    class Meta:
        model = Rating
        fields = '__all__'

class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()
    created_date = serializers.DateTimeField('%d-%m-%Y %H:%M')
    class Meta:
        model = Review
        fields = ['author', 'created_date']


class RoomSerializer(serializers.ModelSerializer):
    room_p = RoomPhotosSerializer(read_only=True, many=True)
    created_date = serializers.DateTimeField('%d-%m-%Y %H:%M')
    class Meta:
        model = Room
        fields = ['room_p','room_name', 'description', 'created_date', 'status', 'types']


class HotelListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    hotel_owner = UserProfileSerializer()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_owner', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField('%d-%m-%Y %H:%M')
    hotel_owner =UserProfileSerializer()
    hotel_photos = HotelPhotosSerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'description', 'created_date', 'hotel_owner', 'hotel_photos', 'rooms',
                  'ratings', 'reviews', 'average_rating']


    def get_average_rating(self, obj):
        return obj.get_average_rating()






class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'



