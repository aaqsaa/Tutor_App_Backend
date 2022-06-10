from email.mime import image
from pyexpat import model
from rest_framework import serializers
from .models import GigPackages, Gigs, Orders,Teachers, Reviews, OrderRequest,GigRating



class GigsSerializer(serializers.ModelSerializer):
    print("I am in serializer")

    class Meta:
        model=Gigs
        fields=('gig_id','name','desc','Startingprice','teacher')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=GigPackages
        fields='__all__'
class StudentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'

class OrderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderRequest
        fields='__all__'
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=GigRating
        feilds='rating'

class OrdersSerializer(serializers.Serializer):
    class Meta:
        model=Orders
        fields='__all__'


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields=('fullname','desc','image')
# class DemoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=demo
        # fields='__all__'