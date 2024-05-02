from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

#import the model 
from .models import coverAndglassCategroy,ProductModel,ProductSize,CoverAndGlassProduct,Warranty,Cover_Color


#import serializer 
from .serializer import coverAndglassCategorySerializer,CoverAndGlassProductSerializer,ProductModelSerializer,ProductSizeSerializer,WarrantySerializer,CoverColorSerializer




class coverAndglassCategoryViewset(viewsets.ModelViewSet):
    queryset = coverAndglassCategroy.objects.all()
    serializer_class = coverAndglassCategorySerializer
    

class CoverColorViewsets(viewsets.ModelViewSet):
    queryset = Cover_Color.objects.all()
    serializer_class = CoverColorSerializer
    

class ProductModelViewset(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    

class ProductSizeViewset(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer
    


class WarrantyViewset(viewsets.ModelViewSet):
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer
    


class CoverAndGlassProductViewset(viewsets.ModelViewSet):
    queryset = CoverAndGlassProduct.objects.all()
    serializer_class = CoverAndGlassProductSerializer
    

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        serializer = self.get_serializer(queryset,many=True)

        for product in serializer.data:
            discount_price = product["price"] * (1 - product['discount'] / 100)
            product['current_price'] = discount_price
        return Response(serializer.data)

