from rest_framework import serializers
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class BookingSerializer(serializers.ModelSerializer):
  class Meta:
      model = Booking
      fields = ['name', 'no_of_guests', 'booking_date']


class MenuSerializer(serializers.ModelSerializer):
  class Meta:
      model = Menu
      fields = ['id', 'title', 'price', 'inventory']
      read_only = ['id']