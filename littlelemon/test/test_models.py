from django.test import TestCase
from restaurant.models import Booking, MenuItem
from django.utils import timezone

class BookingTest(TestCase):
    def setUp(self):
        self.today = timezone.now().date()
        self.booking = Booking.objects.create(name="Alicia", no_of_guests=4, booking_date=self.today)
        
    def test_booking_str_method(self):
        self.assertEqual(str(self.booking), f"Alicia: {self.today}")

    def test_booking_fields(self):
        self.assertEqual(self.booking.name, "Alicia")
        self.assertEqual(self.booking.no_of_guests, 4)
        self.assertIsNotNone(self.booking.booking_date)

class MenuItemTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(title="Pizza", price=9.99, inventory=10)
    
    def test_menu_str_method(self):
        self.assertEqual(str(self.menu_item), "Pizza : 9.99")
        
    def test_menu_fields(self):
        self.assertEqual(self.menu_item.title, "Pizza")
        self.assertEqual(self.menu_item.price, 9.99)
        self.assertEqual(self.menu_item.inventory, 10)