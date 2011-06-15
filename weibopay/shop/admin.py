from weibopay.shop.models import Product,PurchaseRecord
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    pass

class PurchaseRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(PurchaseRecord, PurchaseRecordAdmin)
