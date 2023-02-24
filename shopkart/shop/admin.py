from django.contrib import admin
from . models import *
from .category_models import *
# Register your models here.
admin.site.register(catagory)
admin.site.register(product)
admin.site.register(MobileCategory)
admin.site.register(LaptopCategory)
admin.site.register(BooksCategory)