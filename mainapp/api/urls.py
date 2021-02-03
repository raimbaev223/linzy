from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

urlpatterns = [

]

urlpatterns += router.urls
