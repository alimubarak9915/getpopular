from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from smm import models


@admin.register(models.Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['category_name']
    list_filter = ['category_name']


@admin.register(models.SmmServices)
class SmmServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['service_name', 'service_price', 'service_tag']
    list_filter = ['category']


@admin.register(models.Orders)
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'smm_service', 'is_paid', 'status']
    list_filter = ['is_paid', 'status']
    list_editable = ['status']
    search_fields = ('user__email',)


@admin.register(models.Wallet)
class WalletAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user', 'wallet_balance']
