from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets


#import the model 
from .models import PhoneCategory,PhoneColor,PhoneSpecification,PhoneDescription,PhoneWarranty,PhoneTabletProduct,PhoneNetwork,PhoneType,PhoneSim,PhoneStorage


#import the serailzer 
from .serializer import PhoneCategorySerailzer,PhoneColorSerailzer,PhoneSpecificationSerailzer,PhoneDescriptionSerailzer,PhoneWarrantySerailzer,PhoneTabletProductSerailzer,PhoneNetworkSerailzer,PhoneTypeSerailzer,PhoneSimSerailzer,PhoneStorageSerailzer


class PhoneCategoryViewsets(viewsets.ModelViewSet):
    queryset = PhoneCategory.objects.all()
    serializer_class = PhoneCategorySerailzer

class PhoneColorViewsets(viewsets.ModelViewSet):
    queryset = PhoneColor.objects.all()
    serializer_class = PhoneColorSerailzer

class PhoneSpecificationViewsets(viewsets.ModelViewSet):
    queryset = PhoneSpecification.objects.all()
    serializer_class = PhoneSpecificationSerailzer

class PhoneDescriptionViewsets(viewsets.ModelViewSet):
    queryset = PhoneDescription.objects.all()
    serializer_class = PhoneDescriptionSerailzer

class PhoneWarrantyViewsets(viewsets.ModelViewSet):
    queryset = PhoneWarranty.objects.all()
    serializer_class = PhoneWarrantySerailzer

class PhoneNetworkViewsets(viewsets.ModelViewSet):
    queryset = PhoneNetwork.objects.all()
    serializer_class = PhoneNetworkSerailzer

class PhoneTypeViewsets(viewsets.ModelViewSet):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeSerailzer

class PhoneSimViewsets(viewsets.ModelViewSet):
    queryset = PhoneSim.objects.all()
    serializer_class = PhoneSimSerailzer

class PhoneStorageViewsets(viewsets.ModelViewSet):
    queryset = PhoneStorage.objects.all()
    serializer_class = PhoneStorageSerailzer

class PhoneTabletProductViewsets(viewsets.ModelViewSet):
    queryset = PhoneTabletProduct.objects.all()
    serializer_class = PhoneTabletProductSerailzer


    def list(self, request, *args, **kwagrs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset , many=True)

        for product in serializer.data:
            discount_price = product["price"] * (1 - product['discount'] / 100)
            product['current_price'] = discount_price
        return Response(serializer.data) 
