from django.contrib import admin
from .models import Food, Order

admin.site.site_header = "Online Shop Administration"
admin.site.site_title = "Online Shop Administration"
admin.site.index_title = "Online Shop Administration"
admin.site.register(Food)
admin.site.register(Order)
