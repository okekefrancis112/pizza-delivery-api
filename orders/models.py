# from webbrowser import get
# from django.db import models
# from django.contrib.auth import get_user_model

# # Create your models here.

# User = get_user_model()

# class Order(models.Model):
    
#     SIZES = (
#         ('SMALL', 'small'),
#         ('MEDIUM', 'medium'),
#         ('LARGE', 'large'),
#         ('EXTRA_LARGE', 'extra_large')
#     )
    
#     ORDER_STATUS = (
#         ('PENDING', 'pending'),
#         ('IN_TRANSIT', 'in_transit'),
#         ('DELIVERED', 'delivered')
#     )
    
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     size = models.CharField(max_length=20, choices=SIZES, default=[0][0])
#     order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default=[0][0])
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Order {self.size} by {self.customer.id}"
    
    
from django.db import models
from django.contrib.auth import get_user_model



User=get_user_model()

# Create your models here.
class Order(models.Model):
    PIZZA_SIZES=(
        ('SMALL','Small'),
        ('MEDIUM','Medium'),
        ('LARGE','Large'),
        ('EXTRA_LARGE','Extra_Large'),
    )

    ORDER_STATUSES=(
        ('PENDING','Pending'),
        ('IN_TRANSIT','In_Transit'),
        ('DELIVERED','delivered')
    )

    order_status=models.CharField(max_length=25,choices=ORDER_STATUSES,default=ORDER_STATUSES[0][0])
    size=models.CharField(max_length=25,choices=PIZZA_SIZES,default=PIZZA_SIZES[0][0])
    quantity=models.IntegerField()
    flavour=models.CharField(max_length=40, blank=True)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    placed_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.flavour} by {self.customer}>"
