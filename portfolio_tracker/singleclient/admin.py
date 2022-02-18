from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['fpk', 'name', 'is_active']
    search_fields = ['fpk']
    ordering = ['fpk']


class AccountTypeAdmin(admin.ModelAdmin):
    search_fields = ['account_type']
    ordering = ['account_type']


class AccountAdmin(admin.ModelAdmin):
    list_display = ['fpk', 'clientid','account_type']
    search_fields = ['fpk','clientid']
    ordering = ['fpk','clientid']


class SecurityAssetClassAdmin(admin.ModelAdmin):
    search_fields = ['security_asset_class']
    ordering = ['security_asset_class']


class SecurityAdmin(admin.ModelAdmin):
    list_display = ['fpk','name','asset_class']
    search_fields = ['fpk']
    ordering = ['fpk']

class SecurityPriceAdmin(admin.ModelAdmin):
    list_display = ['securityid','date','price']
    search_fields = ['securityid']
    ordering = ['securityid','date']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['accountid','security',
                    'trade_date','trx_type',
                    'trx_amt','trx_qty']
    search_fields = ['accountid','securityid','trx_type']
    ordering = ['accountid','security','trade_date']


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(AccountType,AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(SecurityAssetClass, SecurityAssetClassAdmin)
admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityPrice, SecurityPriceAdmin)
admin.site.register(Transaction, TransactionAdmin)