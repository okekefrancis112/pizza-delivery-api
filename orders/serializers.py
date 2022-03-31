# from email.policy import default
# from .models import Order
# from rest_framework import serializers

# class OrderCreationSerializer(serializers.ModelSerializer):
    
#     size =serializers.CharField(max_length=20)
#     order_status = serializers.HiddenField(default='PENDING')
#     quantity = serializers.IntegerField()
    
#     class Meta:
#         model = Order
#         fields = ['id', 'size', 'order_status', 'quantity']
        
# class OrderDetailSerializer(serializers.ModelSerializer):
    
#     size =serializers.CharField(max_length=20)
#     order_status = serializers.CharField(default='PENDING')
#     quantity = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
    
#     class Meta:
#         model = Order
#         fields = ['id', 'size', 'order_status', 'quantity', 'created_at', 'updated_at']
        
# class OrderStatusUpdateSerializer(serializers.ModelSerializer):
#     order_status = serializers.CharField(default='PENDING')
    
#     class Meta:
#         model = Order
#         fields = ['order_status']

from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    flavour=serializers.CharField(max_length=40)

    class Meta:
        model=Order 
        fields=['order_status', 'size', 'quantity','flavour']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=25)

    class Meta:
        model=Order
        fields=['order_status']