from django.contrib import admin

from restaurant import models

admin.site.register(models.Booking)
admin.site.register(models.MenuItem)