# from email.mime import image
# from rest_framework import serializers
# from .models import Gigs

# # class BinaryField(serializers.Field):
# #     image=serializers.CharField()
# #     print("image in serialzier::: ",image)

# #     def to_representation(self, value):
# #         print("vaaaaalllluuuueeee: ",value)
# #         return value.decode('utf-8')

#     # def to_internal_value(self, value):
#     #     return value.encode('utf-8')

# class GigsSerializer(serializers.ModelSerializer):
#     print("I am in serializer")

#     class Meta:
#         model=Gigs
#         fields=('gig_id','name','desc','image','package','price')

#         # Gigs.image=serializers.CharField()
#         # print("image in serialzier:::kjfhskujhfukhfukdshfuhfudshfushgfudsghuoaguoagbvufgbodfh ")

#         # print("image in serialzier::: ",Gigs.image)
#         # gig=Gigs.objects.all()
#         # print("zainabbbbbbbbbbbbbbbbbbbbbbb:::::",gig.image.decode("UTF-8"))

#         # image=serializers.CharField()
#         # print("image in serialzier::: ",image)
        

#         # fields= '__all__'
#     # image = BinaryField()


# # class DemoSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model=demo
# #         fields='__all__'