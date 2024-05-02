from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters,pagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
#import the  model 
from .models import Blog,Reviewer,Benner
#import the reviewer 
from .serializer import BlogSerializer,ReviewSerializer,BennerSerializer




##################### try to again ##################

from cemera.models import CameraProduct
from cemera.serializer import CameraProductSerializer


from coverAndglass.models import CoverAndGlassProduct
from coverAndglass.serializer import CoverAndGlassProductSerializer



from loptobAnddesktop.models import laptobAnddesktopProduct
from loptobAnddesktop.serializer import LaptobAndDesktopProductSerializer


from phoneAndtablet.models import PhoneTabletProduct
from phoneAndtablet.serializer import PhoneTabletProductSerailzer


from powerAndaccessories.models import PowerTabletProduct
from powerAndaccessories.serializer import PowerTabletProductSerializer


from smartWatch.models import smartWatchProduct
from smartWatch.serializer import smartWatchProductSerializer


from soundAndequipment.models import SoundAndequipmentProduct
from soundAndequipment.serializer import SoundAndequipmentProductSerializer


class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [


        {'queryset': CameraProduct.objects.all(), 'serializer_class': CameraProductSerializer},

        {'queryset': CoverAndGlassProduct.objects.all(), 'serializer_class': CoverAndGlassProductSerializer},

        {'queryset': laptobAnddesktopProduct.objects.all(), 'serializer_class': LaptobAndDesktopProductSerializer},


        {'queryset': PhoneTabletProduct.objects.all(), 'serializer_class': PhoneTabletProductSerailzer},


        {'queryset': PowerTabletProduct.objects.all(), 'serializer_class': PowerTabletProductSerializer},

        {'queryset': smartWatchProduct.objects.all(), 'serializer_class': smartWatchProductSerializer},

        {'queryset': SoundAndequipmentProduct.objects.all(), 'serializer_class': SoundAndequipmentProductSerializer},
        
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']








class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ReviewViewsets(viewsets.ModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewSerializer

class BennerViewsets(viewsets.ModelViewSet):
    queryset = Benner.objects.all()
    serializer_class = BennerSerializer
