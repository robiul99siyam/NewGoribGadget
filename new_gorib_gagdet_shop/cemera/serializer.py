from rest_framework import serializers
#import the model 
from .models import CameraCategory,CameraModel,CameraProduct,CameraType,CameraWarranty


class cameraCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraCategory
        fields = '__all__'


class CameraModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraModel
        fields = '__all__'


class CameraTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraType
        fields = '__all__'


class CameraWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraWarranty
        fields = '__all__'


class CameraProductSerializer(serializers.ModelSerializer):
    category = CameraCategory()
    model = CameraModelSerializer()
    camera_type = CameraTypeSerializer()
    warranty = CameraWarrantySerializer()
    class Meta:
        model = CameraProduct
        fields = '__all__'