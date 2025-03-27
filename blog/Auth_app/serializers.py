from rest_framework import serializers
from .models import Contact

# class ContactSerilizer(serializers.Serializer):
#     fullname=serializers.CharField()
#     email=serializers.EmailField()
#     mobile=serializers.CharField()
#     message=serializers.CharField()
    

class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"