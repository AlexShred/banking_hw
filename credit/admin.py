from django.contrib import admin

from .models import Client, Account, Credit


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'citizenship', 'birth_year', 'work_place']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['number', 'account_type', 'client']

    @admin.register(Credit)
    class CreditAdmin(admin.ModelAdmin):
        list_display = ['sum', 'date', 'account']
