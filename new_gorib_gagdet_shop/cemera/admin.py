from django.contrib import admin

#import the model 
from .models import CameraCategory,CameraModel,CameraProduct,CameraType,CameraWarranty

moel_register = [CameraCategory,CameraModel,CameraType]


class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in moel_register:
    admin.site.register(model,AdminModel)


admin.site.register(CameraProduct)
admin.site.register(CameraWarranty)