from django.contrib import admin
from .models import User

@admin.register(User)
# Register your models here.
class User(admin.ModelAdmin):
    list_display = ['id','full_name', 'username', 'telegram_id', 'created_at','updated_at']
    search_fields = ['id','full_name', 'username','telegram_id']
