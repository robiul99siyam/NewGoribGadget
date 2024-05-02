from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()



router.register("sound/Specificaion",views.soundSpecificaionViewsets)
router.register("Sound/Description",views.SoundDescriptionViewsets)
router.register("Sound/Category",views.SoundCategoryViewsets)
router.register("Sound/color",views.SoundcolorViewsets)
router.register("Sound/plug",views.SoundPlugViewsets)
router.register("Sound/type",views.SoundTypeViewsets)
router.register("Sound/Warranty",views.SoundWarrantyViewsets)
router.register("Sound/And/equipment/Product/add",views.SoundAndequipmentProductViewsets)

urlpatterns = [
  path("",include(router.urls))
]