from rest_framework import serializers


#import the model 
from .models import soundSpecificaion,SoundDescription,SoundAndequipmentProduct,SoundCategory,Soundcolor,SoundPlug,SoundType,SoundWarranty


class SoundSpecificaionSerializer(serializers.ModelSerializer):
    class Meta:
        model = soundSpecificaion
        fields = '__all__'


class SoundCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundCategory
        fields = '__all__'


class SoundDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundDescription
        fields = '__all__'


class SoundcolorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soundcolor
        fields = '__all__'


class SoundPlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundPlug
        fields = '__all__'


class SoundTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundType
        fields = '__all__'


class SoundWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundWarranty
        fields = '__all__'


class SoundAndequipmentProductSerializer(serializers.ModelSerializer):
    category = SoundCategorySerializer()
    warranty = SoundWarrantySerializer()
    specification = SoundSpecificaionSerializer()
    description = SoundDescriptionSerializer()

    class Meta:
        model = SoundAndequipmentProduct
        fields = '__all__'
        ordering = ['price']