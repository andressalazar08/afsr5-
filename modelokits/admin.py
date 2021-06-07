from django.contrib import admin

# Register your models here.
from .models import Kits, KitsProducts, Kit_Beneciciary, KitsPrincipal

class KitAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class KitsProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class Kit_BeneciciaryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Kits, KitAdmin)
admin.site.register(KitsProducts, KitsProductsAdmin)
admin.site.register(Kit_Beneciciary, Kit_BeneciciaryAdmin)
admin.site.register(KitsPrincipal)