from django.contrib import admin

from .models import soundSpecificaion,SoundDescription,SoundAndequipmentProduct,SoundCategory,Soundcolor,SoundPlug,SoundType,SoundWarranty

model_register = [SoundCategory,Soundcolor,SoundPlug,SoundType,SoundWarranty]


class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in model_register:
    admin.site.register(model,AdminModel)


admin.site.register(soundSpecificaion)
admin.site.register(SoundDescription)
admin.site.register(SoundAndequipmentProduct)
