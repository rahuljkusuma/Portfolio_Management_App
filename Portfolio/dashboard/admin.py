from django.contrib import admin

from .models import Stock, Gold

# Register your models here.

admin.site.register(Stock)
admin.site.register(Gold)

# @admin.register(Stock)
# class CategoryAdmin(admin.ModelAdmin):
#     # list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
