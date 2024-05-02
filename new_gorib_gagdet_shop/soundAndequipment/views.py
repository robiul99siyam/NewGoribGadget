from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
# import the model.
from .models import soundSpecificaion,SoundDescription,SoundAndequipmentProduct,SoundCategory,Soundcolor,SoundPlug,SoundType,SoundWarranty


from .serializer import SoundSpecificaionSerializer,SoundDescriptionSerializer,SoundAndequipmentProductSerializer,SoundCategorySerializer,SoundcolorSerializer,SoundPlugSerializer,SoundTypeSerializer,SoundWarrantySerializer


class soundSpecificaionViewsets(viewsets.ModelViewSet):
    queryset = soundSpecificaion.objects.all()
    serializer_class = SoundSpecificaionSerializer


class SoundDescriptionViewsets(viewsets.ModelViewSet):
    queryset = SoundDescription.objects.all()
    serializer_class = SoundDescriptionSerializer


class SoundCategoryViewsets(viewsets.ModelViewSet):
    queryset = SoundCategory.objects.all()
    serializer_class = SoundCategorySerializer


class SoundcolorViewsets(viewsets.ModelViewSet):
    queryset = Soundcolor.objects.all()
    serializer_class = SoundcolorSerializer


class SoundPlugViewsets(viewsets.ModelViewSet):
    queryset = SoundPlug.objects.all()
    serializer_class = SoundPlugSerializer


class SoundTypeViewsets(viewsets.ModelViewSet):
    queryset = SoundType.objects.all()
    serializer_class = SoundTypeSerializer


class SoundWarrantyViewsets(viewsets.ModelViewSet):
    queryset = SoundWarranty.objects.all()
    serializer_class = SoundWarrantySerializer


class SoundAndequipmentProductViewsets(viewsets.ModelViewSet):
    queryset = SoundAndequipmentProduct.objects.all()
    serializer_class = SoundAndequipmentProductSerializer

