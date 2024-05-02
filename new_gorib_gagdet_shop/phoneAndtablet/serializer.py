from rest_framework import serializers

#import the model 
from .models import PhoneCategory,PhoneColor,PhoneSpecification,PhoneDescription,PhoneWarranty,PhoneTabletProduct,PhoneSim,PhoneNetwork,PhoneStorage,PhoneType


class PhoneCategorySerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneCategory
        fields = '__all__'


class PhoneColorSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneColor
        fields = '__all__'


class PhoneSpecificationSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneSpecification
        fields = '__all__'


class PhoneDescriptionSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneDescription
        fields = '__all__'


class PhoneSimSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneSim
        fields = '__all__'


class PhoneNetworkSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneNetwork
        fields = '__all__'


class PhoneStorageSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneStorage
        fields = '__all__'

class PhoneTypeSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneType
        fields = '__all__'

class PhoneWarrantySerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneWarranty
        fields = '__all__'

class PhoneTabletProductSerailzer(serializers.ModelSerializer):
    class Meta:
        model =PhoneTabletProduct
        fields = '__all__'
