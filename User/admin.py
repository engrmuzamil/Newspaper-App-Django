from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import ChangeForm, CreateForm

class CustomUserAdmin(UserAdmin):
    add_form = CreateForm
    form = ChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'PhoneNo']

admin.site.register(CustomUser, CustomUserAdmin)