from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

# import the model
from .models import smartWatchCategroy,smartWatchSize,smartWatchType,SmartWatchSpecificaion,SmartWatchDescription,SmartWatchEdition,SmartWatchNetwork,SmartWatchStrap,SmartWatchWarranty,smartWatchProduct,color

#import the serailzer 

from .serializer import smartWatchCategroySerializer,smartWatchSizeSerializer,smartWatchTypeSerializer,SmartWatchSpecificaionSerializer,SmartWatchDescriptionSerializer,SmartWatchEditionSerializer,SmartWatchNetworkSerializer,SmartWatchStrapSerializer,SmartWatchWarrantySerializer,smartWatchProductSerializer,ColorSerializer


class smartWatchCategroyViewset(viewsets.ModelViewSet):
    queryset = smartWatchCategroy.objects.all()
    serializer_class = smartWatchCategroySerializer


class smartWatchSizeViewset(viewsets.ModelViewSet):
    queryset = smartWatchSize.objects.all()
    serializer_class = smartWatchSizeSerializer


class smartWatchTypeViewset(viewsets.ModelViewSet):
    queryset = smartWatchType.objects.all()
    serializer_class = smartWatchTypeSerializer


class SmartWatchSpecificaionViewset(viewsets.ModelViewSet):
    queryset = SmartWatchSpecificaion.objects.all()
    serializer_class = SmartWatchSpecificaionSerializer


class SmartWatchDescriptionViewset(viewsets.ModelViewSet):
    queryset = SmartWatchDescription.objects.all()
    serializer_class = SmartWatchDescriptionSerializer


class SmartWatchEditionViewset(viewsets.ModelViewSet):
    queryset = SmartWatchEdition.objects.all()
    serializer_class = SmartWatchEditionSerializer


class SmartWatchNetworkViewset(viewsets.ModelViewSet):
    queryset = SmartWatchNetwork.objects.all()
    serializer_class = SmartWatchNetworkSerializer


class SmartWatchStrapViewset(viewsets.ModelViewSet):
    queryset = SmartWatchStrap.objects.all()
    serializer_class = SmartWatchStrapSerializer


class SmartWatchWarrantyViewset(viewsets.ModelViewSet):
    queryset = SmartWatchWarranty.objects.all()
    serializer_class = SmartWatchWarrantySerializer


class SmartWatchcolorViewset(viewsets.ModelViewSet):
    queryset = color.objects.all()
    serializer_class = ColorSerializer



class smartWatchProducViewsets(viewsets.ModelViewSet):
    queryset = smartWatchProduct.objects.all()
    serializer_class = smartWatchProductSerializer

    def list(self, request, *args, **kwagrs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset , many=True)

        for product in serializer.data:
            discount_price = product["price"] * (1 - product['discount'] / 100)
            product['current_price'] = discount_price
        return Response(serializer.data) 




