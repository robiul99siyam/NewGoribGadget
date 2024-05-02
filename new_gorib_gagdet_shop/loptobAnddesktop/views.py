from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

#import the model
from .models import LaptobStorage,LaptobRim,LaptobWarranty,LaptopCategory,LaptopSpecification,LaptobDescription,laptobAnddesktopProduct
 
#import the seriaiizer 

from .serializer import LaptobStorageSerializer,LaptobRamSerializer,LaptobWarrantySerializer,LaptopCategorySerializer,LaptopSpecificationSerializer,LaptobDescriptionSerializer,LaptobAndDesktopProductSerializer


class LaptobStorageViewsets(viewsets.ModelViewSet):
    queryset = LaptobStorage.objects.all()
    serializer_class = LaptobStorageSerializer


class LaptobRamViewsets(viewsets.ModelViewSet):
    queryset = LaptobRim.objects.all()
    serializer_class = LaptobRamSerializer


class LaptobWarrantyViewsets(viewsets.ModelViewSet):
    queryset = LaptobWarranty.objects.all()
    serializer_class = LaptobWarrantySerializer


class LaptopCategoryViewsets(viewsets.ModelViewSet):
    queryset = LaptopCategory.objects.all()
    serializer_class = LaptopCategorySerializer


class LaptopSpecificationViewsets(viewsets.ModelViewSet):
    queryset = LaptopSpecification.objects.all()
    serializer_class = LaptopSpecificationSerializer


class LaptobDescriptionViewsets(viewsets.ModelViewSet):
    queryset = LaptobDescription.objects.all()
    serializer_class = LaptobDescriptionSerializer


class laptobAnddesktopProductViewsets(viewsets.ModelViewSet):
    queryset = laptobAnddesktopProduct.objects.all()
    serializer_class = LaptobAndDesktopProductSerializer

    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serailzer = self.get_serializer(queryset,many=True)
        for product in serailzer.data:
            discount_price = product["price"] * (1 - product['discount'] / 100)
            product['current_price'] = discount_price
        return Response(serailzer.data)
        