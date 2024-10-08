from .models import Category,Genders,Products,Comment
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenderSerializer(serializers.Serializer):
    class Meta:
        model = Genders
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Products
        fields = '__all__'


class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'
                                