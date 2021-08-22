from django.contrib import admin
from carts.models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart)
admin.site.register(CartItem)
