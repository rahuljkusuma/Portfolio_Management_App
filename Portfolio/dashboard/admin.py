from django.contrib import admin
from django.forms import models

from .models import Stock, Gold

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ('id', 'name', 'quantity', 'buy_price', 'total', 'buy_date', 'updated')


admin.site.register(Stock, StockAdmin)
admin.site.register(Gold)

# @admin.register(Stock)
# class CategoryAdmin(admin.ModelAdmin):
#     # list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
