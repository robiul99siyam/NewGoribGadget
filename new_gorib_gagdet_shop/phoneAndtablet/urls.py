from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PhoneCategoryViewsets,PhoneColorViewsets,PhoneDescriptionViewsets,PhoneNetworkViewsets,PhoneSpecificationViewsets,PhoneSimViewsets,PhoneWarrantyViewsets,PhoneTypeViewsets,PhoneStorageViewsets,PhoneTabletProductViewsets

router = DefaultRouter()
router.register("Phone/Category",PhoneCategoryViewsets)
router.register("Phone/Color",PhoneColorViewsets)
router.register("Phone/Description",PhoneDescriptionViewsets)
router.register("Phone/Network",PhoneNetworkViewsets)
router.register("Phone/Specification",PhoneSpecificationViewsets)
router.register("Phone/Sim",PhoneSimViewsets)
router.register("Phone/Warranty",PhoneWarrantyViewsets)
router.register("Phone/Type",PhoneTypeViewsets)
router.register("Phone/Storage",PhoneStorageViewsets)
router.register("Phone/Tablet/Product/add",PhoneTabletProductViewsets)


urlpatterns = [
  path("",include(router.urls))
]