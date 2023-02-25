from django.contrib import admin
from .models import *
from .category_models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

admin.site.register(LaptopCategory)
admin.site.register(MobileCategory)