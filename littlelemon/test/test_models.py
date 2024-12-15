from django.test import TestCase
from LittleLemonAPI.models import Booking, MenuItem
from django.utils import timezone

class BookingTest(TestCase):

    def test_booking_creation(self):
        today = timezone.now().date()
        booking = Booking.objects.create(name="Alicia", no_of_guests=4, booking_date=today)
        self.assertEqual(str(booking), f"Alicia: {today}")


class MenuItemTest(TestCase):

    def test_menu_item_creation(self):
        menu_item = MenuItem.objects.create(title="Pizza", price=9.99, inventory=10)
        self.assertEqual(str(menu_item), "Pizza : 9.99")