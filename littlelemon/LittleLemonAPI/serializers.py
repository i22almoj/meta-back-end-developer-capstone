from rest_framework import serializers
from django.contrib.auth.models import User
from LittleLemonAPI.models import MenuItem, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        # Return the group name
        return value.name
              
class BookingSerializer(serializers.ModelSerializer):
  class Meta:
      model = Booking
      fields = ['id', 'name', 'no_of_guests', 'booking_date']


class MenuItemSerializer(serializers.ModelSerializer):
  class Meta:
      model = MenuItem
      fields = ['id', 'title', 'price', 'inventory']
      read_only = ['id']