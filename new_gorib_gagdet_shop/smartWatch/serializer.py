from rest_framework import serializers
#import the model 
from .models import smartWatchCategroy,smartWatchSize,smartWatchType,SmartWatchSpecificaion,SmartWatchDescription,SmartWatchEdition,SmartWatchNetwork,SmartWatchStrap,SmartWatchWarranty,smartWatchProduct,color


class smartWatchCategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = smartWatchCategroy
        fields = '__all__'
        

class smartWatchSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = smartWatchSize
        fields = '__all__'

class smartWatchTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = smartWatchType
        fields = '__all__'

class SmartWatchSpecificaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatchSpecificaion
        fields = '__all__'

class SmartWatchDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatchDescription
        fields = '__all__'

class SmartWatchEditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatchEdition
        fields = '__all__'

class SmartWatchStrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatchStrap
        fields = '__all__'

class SmartWatchNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatchNetwork
        fields = '__all__'

class SmartWatchWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartWatchWarranty
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = color
        fields = '__all__'

class smartWatchProductSerializer(serializers.ModelSerializer):
    category = smartWatchCategroySerializer()
    color = ColorSerializer(many=True)
    specification = SmartWatchSpecificaionSerializer()
    description = SmartWatchDescriptionSerializer()
    smartWatchType = smartWatchTypeSerializer()
    smartWatchSize = smartWatchSizeSerializer()
    SmartWatchWarranty = SmartWatchWarrantySerializer()
    SmartWatchStrap = SmartWatchStrapSerializer()
    SmartWatchNetwork = SmartWatchNetworkSerializer()
    SmartWatchEdition = SmartWatchEditionSerializer()

    class Meta:
        model = smartWatchProduct
        fields = '__all__'
        ordering = ['price']
