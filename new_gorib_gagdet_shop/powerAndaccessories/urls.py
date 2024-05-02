from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PowerTabletProductViewsets,PowerWattViewsets,PowerSpecificationViewsets,PowerSizeViewsets,PowerPlugViewsets,PowerModelViewsets,PowerLengthViewsets,PowerDescriptionViewsets,PowerColorViewsets,PowerCategoryViewsets,PowerCapcityViewsets

router = DefaultRouter()

router.register("Power/Capcity",PowerCapcityViewsets)
router.register("Power/Category",PowerCategoryViewsets)
router.register("Power/Color",PowerColorViewsets)
router.register("Power/Description",PowerDescriptionViewsets)
router.register("Power/Length",PowerLengthViewsets)
router.register("Power/Model",PowerModelViewsets)
router.register("Power/Plug",PowerPlugViewsets)
router.register("Power/Size",PowerSizeViewsets)
router.register("Power/Watt",PowerWattViewsets)
router.register("Power/Table/tProduct",PowerTabletProductViewsets)



urlpatterns = [
  path("",include(router.urls))
]