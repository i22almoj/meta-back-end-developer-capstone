from django.test import TestCase
from LittleLemonAPI.models import MenuItem, Booking
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from datetime import date
from django.utils.timezone import now


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


class BookingViewTest(TestCase):

    def setUp(self):
        # Crear usuario y autenticación
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Crear Booking con todos los campos explícitos
        self.booking_explicit = Booking.objects.create(
            name="Alicia",
            no_of_guests=3,
            booking_date=date.today()
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
                "booking_date": str(date.today())
            },
            {
                "id": self.booking_defaults.id,
                "name": "Roberto",
                "no_of_guests": 6,  # Valor por defecto
                "booking_date": str(now().date())  # Valor por defecto
            }
        ]

        # Comparar la respuesta con los datos esperados
        self.assertEqual(response.json(), expected_data)