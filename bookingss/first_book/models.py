from django.db import models
from django .contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


STATUS_BOOK = (
    ('client', 'Client'),
    ('owner', 'Owner')
)

STATUS_CHOICES=(
    ('double room', 'Double room'),
    ('triple room', 'Triple room'),
    ('Family room', 'Family room')
)

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16),
                                                       MaxValueValidator(70)],
                                                       null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    status = models.CharField(max_length=17, choices=STATUS_BOOK, default='client')

    def __str__(self):
       return f'{self.first_name} - {self.last_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    hotel_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.hotel_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_photos', on_delete=models.CASCADE)
    hotel_image =models.ImageField(upload_to='hotel_image', null=True,blank=True)




class Rating(models.Model):
    hotel_rating = models.ForeignKey(Hotel, related_name='ratings', on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг")

    def __str__(self):
        return f"{self.hotel_rating} - {self.user_profile} - {self.stars} stars"


class Room(models.Model):
      hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
      room_name = models.CharField(max_length=32)
      description = models.TextField()
      created_date = models.DateTimeField(auto_now_add=True)

      TYPE_CHOICES=(
      ('free', 'Free'),
      ('booked', 'Booked'),
      ('occupied', 'Occupied')
      )
      types = models.CharField(max_length=32, choices=TYPE_CHOICES, default='booked')
      status = models.CharField(max_length=32, choices=STATUS_CHOICES)

      def __str__(self):
          return self.room_name

class RoomPhotos(models.Model):
    room_p = models.ForeignKey(Room, related_name='room_p', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')


class Review (models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    hotel_review = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.hotel_review}'


class Booking(models.Model):
   book_hotel = models.ForeignKey(Hotel, max_length=32, on_delete=models.CASCADE)
   book_room = models.ForeignKey(Room, max_length=32, on_delete=models.CASCADE)
   book_user= models.ForeignKey( UserProfile, max_length=32, on_delete=models.CASCADE)
   entered = models.DateTimeField(auto_now_add=True)
   got_out = models.DateTimeField(auto_now_add=True)
   hotel_price = models.PositiveIntegerField(default=0)
   status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='double room')

   def __str__(self):
       return f'{self.book_hotel} - {self.book_room}'


