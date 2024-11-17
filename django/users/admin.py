from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'user_id']  # Customize the fields displayed in the admin interface

# Register your models here.
admin.site.register(User, UserAdmin)
