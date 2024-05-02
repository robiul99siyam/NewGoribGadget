from django.contrib import admin

#import the all model 

from .models import LaptobStorage,LaptobRim,LaptobWarranty,LaptopCategory,LaptopSpecification,LaptobDescription,laptobAnddesktopProduct


model_register = [LaptobStorage,LaptobRim,LaptopCategory]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in model_register:
    admin.site.register(model,AdminModel)


admin.site.register(LaptobDescription)
admin.site.register(LaptobWarranty)
admin.site.register(LaptopSpecification)
admin.site.register(laptobAnddesktopProduct)