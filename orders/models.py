from django.db import models
from cart.models import CartItem
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    create = models.DateTimeField(null=False, default=timezone.now)
    complete = models.DateTimeField(null=True)
    status = models.CharField(max_length=256)


class Purchase(models.Model):
    cart_item = models.ForeignKey(CartItem, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
