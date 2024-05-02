from rest_framework import serializers

# import the model 
from .models import PowerCapcity,PowerCategory,PowerColor,PowerDescription,PowerLength,PowerModel,PowerPlug,PowerSize,PowerSpecification,PowerTabletProduct,PowerType,PowerWatt


class PowerCapcitySerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerCapcity
        fields = '__all__'


class PowerColorSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerColor
        fields = '__all__'


class PowerCategorySerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerCategory
        fields = '__all__'


class PowerDescriptionSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerDescription
        fields = '__all__'


class PowerLengthSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerLength
        fields = '__all__'


class PowerModelSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerModel
        fields = '__all__'


class PowerPlugSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlug
        fields = '__all__'


class PowerSizeSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerSize
        fields = '__all__'


class PowerSpecificationSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerSpecification
        fields = '__all__'


class PowerTypeSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerType
        fields = '__all__'


class PowerWattSerailzer(serializers.ModelSerializer):
    class Meta:
        model = PowerWatt
        fields = '__all__'



class PowerTabletProductSerializer(serializers.ModelSerializer):
    category = PowerCapcitySerailzer()
    color = PowerColorSerailzer(many=True)
    specification = PowerSpecificationSerailzer()
    description = PowerDescriptionSerailzer()
    plug = PowerPlugSerailzer()
    watt = PowerWattSerailzer()
    length = PowerLengthSerailzer()

    class Meta:
        model = PowerTabletProduct
        fields = '__all__'
        ordering = ['price']
