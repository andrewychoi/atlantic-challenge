from django.contrib import admin

from orders import models

admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Purchase)
