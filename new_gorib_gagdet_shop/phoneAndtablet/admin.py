from django.contrib import admin

#import the model 
from .models import PhoneCategory,PhoneColor,PhoneSpecification,PhoneDescription,PhoneWarranty,PhoneTabletProduct,PhoneNetwork,PhoneType,PhoneSim,PhoneStorage


model_register = [PhoneCategory,PhoneColor,PhoneNetwork,PhoneType,PhoneSim,PhoneStorage]

class AdminSlugRegister(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']
for model in model_register:
    admin.site.register(model,AdminSlugRegister)



admin.site.register(PhoneSpecification)
admin.site.register(PhoneDescription)
admin.site.register(PhoneWarranty)
admin.site.register(PhoneTabletProduct)