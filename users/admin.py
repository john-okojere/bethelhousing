from django.contrib import admin
from .models import CustomUser, Account

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','fullName', 'email','accountType' , 'is_customer' , 'is_agent' , 'is_agency' ,'is_staff', 'is_active')


@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    list_display = ('profile','yourTitle', 'address','city','state','zipcode','about','facebook','twitter','googlePlus','linkedIn')
