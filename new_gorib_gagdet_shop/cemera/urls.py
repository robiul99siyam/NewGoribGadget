from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("Camare/Category",views.CamareCategoryViewsets)
router.register("Camare/Model",views.CameraModelViewsets)
router.register("Camare/Warranty",views.CameraWarrantyViewsets)
router.register("Camare/type",views.CameraTypeViewsets)
router.register("Camare/Product/add",views.CameraProductViewsets)



urlpatterns = [
  path("",include(router.urls))
]