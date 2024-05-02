from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("Blog",views.BlogViewset)
router.register("review",views.ReviewViewsets)
router.register("benner",views.BennerViewsets)

urlpatterns = [
  path("",include(router.urls)),
  path("textapi/", views.TextAPIView.as_view(), name="textapi"),
]