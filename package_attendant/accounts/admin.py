from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address_1', 'address_2', 'city', 'state', 'zip_code')

  
admin.site.register(UserProfile)



