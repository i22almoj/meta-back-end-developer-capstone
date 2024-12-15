# Meta Backend Capstone Project

## Configuración de Base de datos y migraciones

Se debe crear una base de datos y un usuario root con estas características antes de realizar las migraciones

```jsx
DATABASES = {
  default: {
    ENGINE: "django.db.backends.mysql",
    NAME: "LittleLemon",
    HOST: "localhost",
    PORT: "3306",
    USER: "root",
    PASSWORD: "",
    OPTIONS: {
      init_command: "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  },
};
```

Aplicar las migraciones:

```jsx
python manage.py migrate
```

<br>

## Endpoints de la API

### Endpoint para obtener el token de sesión

```jsx
http://127.0.0.1:8000/auth/token/login
```

### Endpoints de gestión

```jsx
http://127.0.0.1:8000/api/menu-items
http://127.0.0.1:8000/api/menu-items/{menu-itemId}
http://127.0.0.1:8000/api/bookings
http://127.0.0.1:8000/api/bookings/{bookingId}
```

<br>

#### http://127.0.0.1:8000/api/menu-items

| Método | Acción                               | Autorización Token | STATUS CODE |
| ------ | ------------------------------------ | ------------------ | ----------- |
| GET    | Devuelve todos los elementos de menú | Sí                 | 200         |
| POST   | Crea un elemento de menú             | Sí                 | 201         |

<br>

#### http://127.0.0.1:8000/api/menu-items/{menu-itemId}

| Método | Acción                                                | Autorización Token | STATUS CODE |
| ------ | ----------------------------------------------------- | ------------------ | ----------- |
| GET    | Devuelve los detalles de un elemento de menú          | Sí                 | 200         |
| PUT    | Edita un elemento de menú                             | Sí                 | 200         |
| PATCH  | Edita parcialmente los valores de un elemento de menú | Sí                 | 200         |
| DELETE | Elimina un elemento de menú                           | Sí                 | 200         |

<br>

#### http://127.0.0.1:8000/api/bookings

| Método | Acción                      | Autorización Token | STATUS CODE |
| ------ | --------------------------- | ------------------ | ----------- |
| GET    | Devuelve todos las reservas | Sí                 | 200         |
| POST   | Crea una reserva            | Sí                 | 201         |

<br>

#### http://127.0.0.1:8000/api/bookings/{bookingId}

| Método | Acción                               | Autorización Token | STATUS CODE |
| ------ | ------------------------------------ | ------------------ | ----------- |
| GET    | Devuelve los detalles de una reserva | Sí                 | 200         |
| PUT    | Edita un reserva                     | Sí                 | 200         |
| PATCH  | Edita parcialmente una reserva       | Sí                 | 200         |
| DELETE | Elimina una reserva                  | Sí                 | 200         |

<br>

### Endpoints de `djoser`

```jsx
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
```

<br>

## Pruebas

Hay un total de 14 pruebas unitaria para asegurarnos del correcto funcionamiento de los endpoints de la API

Ejecutar los tests:

```jsx
python manage.py test
```

Debe mostrarse algo parecido a esto:

```jsx
Found 14 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............
----------------------------------------------------------------------
Ran 14 tests in 1.820s

OK
Destroying test database for alias 'default'...
```

<br>
