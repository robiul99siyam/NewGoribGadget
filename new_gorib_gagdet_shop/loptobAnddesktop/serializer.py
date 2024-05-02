from rest_framework import serializers

#import the model 

from .models import LaptobStorage,LaptobRim,LaptobWarranty,LaptopCategory,LaptopSpecification,LaptobDescription,laptobAnddesktopProduct



class LaptobStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptobStorage
        fields = '__all__'


class LaptobRamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptobRim
        fields = '__all__'


class LaptobWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptobWarranty
        fields = '__all__'


class LaptopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopCategory
        fields = '__all__'


class LaptopSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopSpecification
        fields = '__all__'


class LaptobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptobDescription
        fields = '__all__'


class LaptobAndDesktopProductSerializer(serializers.ModelSerializer):
    category = LaptopCategorySerializer()
    warranty = LaptobWarrantySerializer()
    specification = LaptopSpecificationSerializer()
    description = LaptobDescriptionSerializer()
    storage = LaptobStorageSerializer()
    ram = LaptobRamSerializer()

    class Meta:
        model = laptobAnddesktopProduct
        fields = '__all__'
        ordering = ['price']
