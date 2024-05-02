from rest_framework import serializers
from .models import Blog,Reviewer,Benner


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = "__all__"

    
class BennerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benner
        fields = "__all__"