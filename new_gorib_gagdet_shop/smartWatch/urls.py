from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()


router.register("smart/Watch/Categroy",views.smartWatchCategroyViewset)
router.register("smar/tWatch/Size",views.smartWatchSizeViewset)
router.register("smart/Watch/Type",views.smartWatchTypeViewset)
router.register("Smart/Watch/Specificaion",views.SmartWatchSpecificaionViewset)
router.register("Smart/Watch/Description",views.SmartWatchDescriptionViewset)
router.register("Smart/Watch/Edition",views.SmartWatchEditionViewset)
router.register("Smart/Watch/Network",views.SmartWatchNetworkViewset)
router.register("Smart/Watch/Strap",views.SmartWatchStrapViewset)
router.register("Smart/Watch/Warranty",views.SmartWatchWarrantyViewset)
router.register("color",views.SmartWatchcolorViewset)
router.register("smart/Watch/Product",views.smartWatchProducViewsets)


urlpatterns = [
  path("",include(router.urls))
]