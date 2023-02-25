from django.urls import path
from . import views
urlpatterns=[
    path("", views.collectionsview, name="collections"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
]