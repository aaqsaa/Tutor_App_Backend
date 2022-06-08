from email.mime import image
from pyexpat import model
from rest_framework import serializers
from .models import GigRating, Gigs,Orders



class GigsSerializer(serializers.ModelSerializer):
    print("I am in serializer")

    class Meta:
        model=Gigs
        fields=('gig_id','name','desc','Startingprice','teacher')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=GigRating
        feilds='rating'

class OrdersSerializer(serializers.Serializer):
    class Meta:
        model=Orders
        fields='__all__'

# class DemoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=demo
#         fields='__all__'