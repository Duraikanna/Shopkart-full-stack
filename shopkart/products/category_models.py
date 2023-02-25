from django.db import models

from products.models import Product


class MobileCategory(models.Model):
    OS_CHOICES          = [
        ("Android", "Android"),
        ("IOS", "IOS"),
        ("Windows", "Windows")
    ]
    Cellular_CHOICES    = [
        ("2G", "2G"),
        ("3G", "3G"),
        ("4G", "4G"),
        ("5G", "5G"),
    ]
    product             = models.OneToOneField(Product, null = True, on_delete=models.CASCADE)
    brand               = models.CharField(max_length=100)
    model               = models.CharField(max_length=100)
    os                  = models.CharField(max_length=30, choices=OS_CHOICES)
    cellular_tech       = models.CharField(max_length=2, choices=Cellular_CHOICES)


class LaptopCategory(models.Model):
    OS_CHOICES          = [
        ("Windows", "Windows"),
        ("Linux",   "Linux"),
        ("Mac",     "Mac"),

    ]

    product             = models.OneToOneField(Product, null=True, on_delete=models.CASCADE)
    brand               = models.CharField(max_length=100)
    series              = models.CharField(max_length=100)
    screen_size         = models.CharField(max_length=100)
    color               = models.CharField(max_length=100)
    cpu_model           = models.CharField(max_length=20)
    ram                 = models.IntegerField()
    operating_system    = models.CharField(max_length=50, choices=OS_CHOICES)
    graphics            = models.IntegerField(null=True)