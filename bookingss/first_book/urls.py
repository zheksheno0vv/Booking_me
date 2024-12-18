from django.urls import path
from .views import *

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='hotel_detail'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                              'delete': 'destroy'}), name='userprofile_detail'),

    path('hotelphotos/', HotelPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotelphotos_list'),
    path('hotelphotos/<int:pk>/', HotelPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                           'delete': 'destroy'}), name='hotelphotos_detail'),

    path('room/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='room_detail'),

    path('roomphotos/', RoomPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='roomphotos_list'),
    path('roomphotos/<int:pk>/', RoomPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                           'delete': 'destroy'}), name='roomphotos_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                           'delete': 'destroy'}), name='review_detail'),

    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='booking_detail'),

]
