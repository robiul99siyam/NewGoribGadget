from django.contrib import admin

#import the model 

from .models import smartWatchCategroy,smartWatchSize,smartWatchType,SmartWatchSpecificaion,SmartWatchDescription,SmartWatchEdition,SmartWatchNetwork,SmartWatchStrap,SmartWatchWarranty,smartWatchProduct,color


model_register = [smartWatchCategroy,smartWatchSize,smartWatchType,SmartWatchStrap,SmartWatchWarranty,SmartWatchEdition,SmartWatchNetwork,color]

class AdminSlugRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']
for model in model_register:
    admin.site.register(model,AdminSlugRegister)

admin.site.register(SmartWatchDescription)
admin.site.register(smartWatchProduct)
admin.site.register(SmartWatchSpecificaion)