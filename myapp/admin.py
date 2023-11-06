from django.contrib import admin

from .models import CustomUser,Category,Product


@admin.register(CustomUser)
class JobCircularAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["first_name"]

admin.site.register(Category)
admin.site.register(Product)