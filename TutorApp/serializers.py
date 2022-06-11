from email.mime import image
from rest_framework import serializers
from .models import Gigs
from .models import CodeEditor

# class BinaryField(serializers.Field):
#     image=serializers.CharField()
#     print("image in serialzier::: ",image)

#     def to_representation(self, value):
#         print("vaaaaalllluuuueeee: ",value)
#         return value.decode('utf-8')

    # def to_internal_value(self, value):
    #     return value.encode('utf-8')

class GigsSerializer(serializers.ModelSerializer):
    print("I am in serializer")

    class Meta:
        model=Gigs
        fields=('gig_id','name','desc','Startingprice')

        # Gigs.image=serializers.CharField()
        # print("image in serialzier:::kjfhskujhfukhfukdshfuhfudshfushgfudsghuoaguoagbvufgbodfh ")

        # print("image in serialzier::: ",Gigs.image)
        # gig=Gigs.objects.all()
        # print("zainabbbbbbbbbbbbbbbbbbbbbbb:::::",gig.image.decode("UTF-8"))

        # image=serializers.CharField()
        # print("image in serialzier::: ",image)
        

        # fields= '__all__'
    # image = BinaryField()


# class DemoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=demo
#         fields='__all__'

class CodeEditorSerializer(serializers.ModelSerializer):
    print("I'm in code editor serializer")
    class Meta:
        model=CodeEditor
        fields='__all__'
