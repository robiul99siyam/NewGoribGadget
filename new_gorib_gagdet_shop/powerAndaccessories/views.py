from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets




# import the model 
from .models import PowerCapcity,PowerCategory,PowerColor,PowerDescription,PowerLength,PowerModel,PowerPlug,PowerSize,PowerSpecification,PowerTabletProduct,PowerType,PowerWatt

#import the serializer 

from .serializer import PowerCapcitySerailzer,PowerCategorySerailzer,PowerColorSerailzer,PowerDescriptionSerailzer,PowerLengthSerailzer,PowerModelSerailzer,PowerPlugSerailzer,PowerSizeSerailzer,PowerSpecificationSerailzer,PowerTabletProductSerializer,PowerTypeSerailzer,PowerWattSerailzer


class PowerCapcityViewsets(viewsets.ModelViewSet):
    queryset = PowerCapcity.objects.all()
    serializer_class = PowerCapcitySerailzer


class PowerCategoryViewsets(viewsets.ModelViewSet):
    queryset = PowerCategory.objects.all()
    serializer_class = PowerCategorySerailzer

class PowerColorViewsets(viewsets.ModelViewSet):
    queryset = PowerColor.objects.all()
    serializer_class = PowerColorSerailzer

class PowerDescriptionViewsets(viewsets.ModelViewSet):
    queryset = PowerDescription.objects.all()
    serializer_class = PowerDescriptionSerailzer

class PowerLengthViewsets(viewsets.ModelViewSet):
    queryset = PowerLength.objects.all()
    serializer_class = PowerLengthSerailzer

class PowerModelViewsets(viewsets.ModelViewSet):
    queryset = PowerModel.objects.all()
    serializer_class = PowerModelSerailzer

class PowerPlugViewsets(viewsets.ModelViewSet):
    queryset = PowerPlug.objects.all()
    serializer_class = PowerPlugSerailzer

class PowerSizeViewsets(viewsets.ModelViewSet):
    queryset = PowerSize.objects.all()
    serializer_class = PowerSizeSerailzer

class PowerSpecificationViewsets(viewsets.ModelViewSet):
    queryset = PowerSpecification.objects.all()
    serializer_class = PowerSpecificationSerailzer

class PowerTypeViewsets(viewsets.ModelViewSet):
    queryset = PowerType.objects.all()
    serializer_class = PowerTypeSerailzer

class PowerWattViewsets(viewsets.ModelViewSet):
    queryset = PowerWatt.objects.all()
    serializer_class = PowerWattSerailzer

class PowerTabletProductViewsets(viewsets.ModelViewSet):
    queryset = PowerTabletProduct.objects.all()
    serializer_class = PowerTabletProductSerializer

    def list(self, request, *args, **kwagrs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset , many=True)

        for product in serializer.data:
            discount_price = product["price"] * (1 - product['discount'] / 100)
            product['current_price'] = discount_price
        return Response(serializer.data) 
