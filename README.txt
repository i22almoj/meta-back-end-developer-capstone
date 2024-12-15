Meta Backend Capstone Project

Configuración de Base de datos y migraciones

Se debe crear una base de datos y un usuario root con estas características antes de realizar las migraciones

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

Aplicar las migraciones:

python manage.py migrate


Endpoints de la API

Endpoint para obtener el token de sesión
http://127.0.0.1:8000/auth/token/login

Endpoints de gestión
http://127.0.0.1:8000/api/menu-items
http://127.0.0.1:8000/api/menu-items/{menu-itemId}
http://127.0.0.1:8000/api/bookings
http://127.0.0.1:8000/api/bookings/{bookingId}

http://127.0.0.1:8000/api/menu-items
Método GET: Devuelve todos los elementos de menú, STATUS	200
Método POST:	Crea un elemento de menú, STATUS	201

http://127.0.0.1:8000/api/menu-items/{menu-itemId}
Método GET:	Devuelve los detalles de un elemento de menú, STATUS 200
Método PUT:	Edita un elemento de menú, STATUS 200
Método PATCH:	Edita parcialmente los valores de un elemento de menú, STATUS 200
Método DELETE:	Elimina un elemento de menú, STATUS 200

http://127.0.0.1:8000/api/bookings
Método GET:	Devuelve todos las reservas, STATUS 200
Método POST:	Crea una reserva, STATUS 201

http://127.0.0.1:8000/api/bookings/{bookingId}
Método GET:	Devuelve los detalles de una reserva, STATUS 200
Método PUT:	Edita un reserva, STATUS 200
Método PATCH:	Edita parcialmente una reserva, STATUS 200
Método DELETE:	Elimina una reserva, STATUS 200

Endpoints de djoser
http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/users/confirm/
http://127.0.0.1:8000/auth/users/resend_activation/
http://127.0.0.1:8000/auth/users/set_password/
http://127.0.0.1:8000/auth/users/reset_password/
http://127.0.0.1:8000/auth/users/reset_password_confirm/
http://127.0.0.1:8000/auth/users/set_username/
http://127.0.0.1:8000/auth/users/reset_username/
http://127.0.0.1:8000/auth/users/reset_username_confirm/



Pruebas
Hay un total de 14 pruebas unitaria para asegurarnos del correcto funcionamiento de los endpoints de la API

Ejecutar los tests:
python manage.py test

Debe mostrarse algo parecido a esto:

Found 14 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............
----------------------------------------------------------------------
Ran 14 tests in 1.820s

OK
Destroying test database for alias 'default'...

