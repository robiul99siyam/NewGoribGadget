from django.contrib import admin

#import the model 
from .models import coverAndglassCategroy,Cover_Color,ProductModel,ProductSize,CoverAndGlassProduct,Warranty


model_register = [coverAndglassCategroy,ProductModel,ProductSize,Cover_Color]

class AdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", 'slug']

for model in model_register:
    admin.site.register(model,AdminModel)

class coverAndglassProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','discount','status']
admin.site.register(CoverAndGlassProduct,coverAndglassProductAdmin)
admin.site.register(Warranty)