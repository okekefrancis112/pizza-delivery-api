# # from dataclasses import fields
# # import email
# from .models import User
# from rest_framework import serializers
# from phonenumber_field.serializerfields import PhoneNumberField

# class UserCreationSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=25)
#     email = serializers.CharField(max_length=80)
#     phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
#     password = serializers.CharField(min_length=8, write_only=True)
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'phone_number', 'password']
        
#     def validate(self, attrs):
#         username_exists=User.objects.filter(username=attrs['username']).exists()
        
#         if username_exists:
#             raise serializers.ValidationError(detail="User with username exists")
        
#         email_exists=User.objects.filter(username=attrs['email']).exists()
        
#         if email_exists:
#             raise serializers.ValidationError(detail="User with email exists")
        
#         phonenumber_exists=User.objects.filter(username=attrs['phone_number']).exists()
        
#         if phonenumber_exists:
#             raise serializers.ValidationError(detail="User with phonenumber exists")
        
#         return super().validate(attrs)
    
#     def create(self, validated_data):
#         user=User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             phone_number=validated_data['phone_number'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

from .models import User
from rest_framework import serializers,status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=40,allow_blank=True)
    email=serializers.EmailField(max_length=80,allow_blank=False)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    password=serializers.CharField(allow_blank=False,write_only=True)


    class Meta:
        model=User
        fields=['id','username', 'email', 'phone_number','password']

    def validate(self,attrs):
        email=User.objects.filter(username=attrs.get('username')).exists()

        if email:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        username=User.objects.filter(username=attrs.get('username')).exists()

        if username:
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)


    def create(self,validated_data):
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user