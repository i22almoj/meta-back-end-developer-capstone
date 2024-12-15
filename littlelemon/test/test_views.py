from django.test import TestCase
from restaurant.models import MenuItem, Booking
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.utils import timezone


class MenuViewTest(TestCase):

    def setUp(self):
        # Crear usuario y autenticación
        self.user = User.objects.create_user(username='testuser', password='testpass')
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {token.key}'

        # Crear MenuItem con todos los campos explícitos
        self.menu_item_explicit = MenuItem.objects.create(
            title="Pizza",
            price=12.99,
            inventory=10
        )

        # Crear MenuItem sin inventory
        self.menu_item_defaults = MenuItem.objects.create(
            title="Sushi",
            price=8.99
        )

    def test_getall(self):
        response = self.client.get(reverse('menu'))

        # Verificar respuesta HTTP
        self.assertEqual(response.status_code, 200)

        # Datos esperados con campo `id`
        expected_data = [
            {
                "id": self.menu_item_explicit.id,
                "title": "Pizza",
                "price": "12.99",
                "inventory": 10
            },
            {
                "id": self.menu_item_defaults.id,
                "title": "Sushi",
                "price": "8.99",
                "inventory": 5  # Valor por defecto
            }
        ]

        # Comparar la respuesta con los datos esperados
        self.assertEqual(response.json(), expected_data)
    
    def test_create_menu_item(self):
        new_data = {
            "title": "Hamburguesa",
            "price": 10.50,
            "inventory": 15
        }
        response = self.client.post(reverse('menu'), new_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.json()["title"], "Hamburguesa")
        self.assertEqual(str(response.json()["price"]), "10.50")
        self.assertEqual(response.json()["inventory"], 15)
        
    def test_edit_menu_item(self):
        updated_data = {"title": "Pizza Vegana", "price": 15.00, "inventory": 20}
        response = self.client.put(reverse('menu-detail', args=[self.menu_item_explicit.id]), updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        self.menu_item_explicit.refresh_from_db()
        self.assertEqual(self.menu_item_explicit.title, "Pizza Vegana")
        self.assertEqual(str(self.menu_item_explicit.price), "15.00")
        self.assertEqual(self.menu_item_explicit.inventory, 20)

    def test_delete_menu_item(self):
        response = self.client.delete(reverse('menu-detail', args=[self.menu_item_explicit.id]))
        self.assertEqual(response.status_code, 204)  # Código para eliminación exitosa

        with self.assertRaises(MenuItem.DoesNotExist):
            MenuItem.objects.get(id=self.menu_item_explicit.id)

    def test_detail_menu_item(self):
        response = self.client.get(reverse('menu-detail', args=[self.menu_item_defaults.id]))
        self.assertEqual(response.status_code, 200)

        expected_data = {
            "id": self.menu_item_defaults.id,
            "title": "Sushi",
            "price": "8.99",
            "inventory": 5
        }

        self.assertEqual(response.json(), expected_data)


class BookingViewTest(TestCase):

    def setUp(self):
        # Crear usuario y autenticación
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.now = timezone.now()
        
        # Crear Booking con todos los campos explícitos
        self.booking_explicit = Booking.objects.create(
            name="Alicia",
            no_of_guests=3,
            booking_date=self.now
        )

        # Crear Booking sin no_of_guests y booking_date
        self.booking_defaults = Booking.objects.create(
            name="Roberto"
        )

    def test_getall(self):
        response = self.client.get(reverse('bookings'))

        # Verificar respuesta HTTP
        self.assertEqual(response.status_code, 200)
        
        # Datos esperados
        expected_data = [
            {
                "id": self.booking_explicit.id,
                "name": "Alicia",
                "no_of_guests": 3,
                "booking_date": self.booking_explicit.booking_date.astimezone(timezone.get_current_timezone()).strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "id": self.booking_defaults.id,
                "name": "Roberto",
                "no_of_guests": 6,  # Valor por defecto
                "booking_date": self.booking_defaults.booking_date.astimezone(timezone.get_current_timezone()).strftime("%Y-%m-%d %H:%M:%S")
            }
        ]

        # Comparar la respuesta con los datos esperados
        self.assertEqual(response.json(), expected_data)
    
    def test_create_booking(self):
        booking_data = {
            "name": "Pedro",
            "no_of_guests": 4,
        }
        response = self.client.post(reverse('bookings'), booking_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.json()["name"], "Pedro")
        self.assertEqual(response.json()["no_of_guests"], 4)
            
    def test_edit_booking(self):
        updated_data = {"name": "Carlos", "no_of_guests": 5}
        response = self.client.put(reverse('booking-detail', args=[self.booking_explicit.id]), updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        self.booking_explicit.refresh_from_db()
        self.assertEqual(self.booking_explicit.name, "Carlos")
        self.assertEqual(self.booking_explicit.no_of_guests, 5)

    def test_delete_booking(self):
        response = self.client.delete(reverse('booking-detail', args=[self.booking_defaults.id]))
        self.assertEqual(response.status_code, 204)

        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(id=self.booking_defaults.id)

    def test_detail_booking(self):
        response = self.client.get(reverse('booking-detail', args=[self.booking_explicit.id]))
        self.assertEqual(response.status_code, 200)

        expected_data = {
            "id": self.booking_explicit.id,
            "name": "Alicia",
            "no_of_guests": 3,
            "booking_date": self.booking_explicit.booking_date.astimezone(timezone.get_current_timezone()).strftime("%Y-%m-%d %H:%M:%S")
        }
        self.assertEqual(response.json(), expected_data)