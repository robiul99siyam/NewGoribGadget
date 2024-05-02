from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("cover/and/glass/categroy",views.coverAndglassCategoryViewset)
router.register("cover/and/glass/product/model",views.ProductModelViewset)
router.register("cover/and/glass/product/size", views.ProductSizeViewset)
router.register("cover/and/glass/color",views.CoverColorViewsets)
router.register("cover/and/glass/product/Warranty", views.WarrantyViewset)
router.register("cover/and/glass/product/add", views.CoverAndGlassProductViewset)
urlpatterns = [
   path("",include(router.urls))
]
