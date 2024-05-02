from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response

#import the model 
from .models import CameraCategory,CameraModel,CameraProduct,CameraType,CameraWarranty


#import the serialzer 

from .serializer import cameraCategorySerializer,CameraModelSerializer,CameraProductSerializer,CameraTypeSerializer,CameraWarrantySerializer


class CamareCategoryViewsets(viewsets.ModelViewSet):
    queryset = CameraCategory.objects.all()
    serializer_class = cameraCategorySerializer



class CameraModelViewsets(viewsets.ModelViewSet):
    queryset = CameraModel.objects.all()
    serializer_class = CameraModelSerializer



class CameraTypeViewsets(viewsets.ModelViewSet):
    queryset = CameraType.objects.all()
    serializer_class = CameraTypeSerializer



class CameraWarrantyViewsets(viewsets.ModelViewSet):
    queryset = CameraWarranty.objects.all()
    serializer_class = CameraWarrantySerializer





class CameraProductViewsets(viewsets.ModelViewSet):
    queryset = CameraProduct.objects.all()
    serializer_class = CameraProductSerializer

    def list (self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)

        for product in serializer.data:
            discount_price = product["price"] * (1 - product['discount'] / 100)
            product['current_price'] = discount_price
        return Response(serializer.data) 

   
