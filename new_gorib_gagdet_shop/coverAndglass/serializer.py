from rest_framework import serializers

#import the model 
from .models import coverAndglassCategroy,ProductModel,ProductSize,CoverAndGlassProduct,Warranty,Cover_Color



class coverAndglassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = coverAndglassCategroy
        fields = '__all__'
        

class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'
        
        

class CoverColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover_Color
        fields = '__all__'
        
# 
class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'
        

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'
        
class CoverAndGlassProductSerializer(serializers.ModelSerializer):

    category = coverAndglassCategorySerializer()
    product_model = ProductModelSerializer()
    product_size = ProductSizeSerializer()
    warranty = WarrantySerializer()  
    # Cover_Color = ColorSerializer(many=True)

    class Meta:
        model = CoverAndGlassProduct
        fields = '__all__'
