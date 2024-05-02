from django.contrib import admin

# import the model 
from .models import PowerCapcity,PowerCategory,PowerColor,PowerDescription,PowerLength,PowerModel,PowerPlug,PowerSize,PowerSpecification,PowerTabletProduct,PowerType,PowerWatt

model_register = [PowerColor,PowerPlug,PowerCapcity,PowerCategory,PowerLength,PowerModel,PowerSize,PowerType,PowerWatt]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in model_register:
    admin.site.register(model,AdminModel)

admin.site.register(PowerDescription)
admin.site.register(PowerSpecification)
admin.site.register(PowerTabletProduct)