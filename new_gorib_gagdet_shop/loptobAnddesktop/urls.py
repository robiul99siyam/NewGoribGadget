from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("Laptob/Storage",views.LaptobStorageViewsets)
router.register("Laptob/Ram",views.LaptobRamViewsets)
router.register("Laptob/Warranty",views.LaptobWarrantyViewsets)
router.register("Laptop/Category",views.LaptopCategoryViewsets)
router.register("Laptop/Specification",views.LaptopSpecificationViewsets)
router.register("Laptob/Description",views.LaptobDescriptionViewsets)
router.register("laptob/And/desktop/Product/add",views.laptobAnddesktopProductViewsets)
urlpatterns = [
   path("",include(router.urls))
]
