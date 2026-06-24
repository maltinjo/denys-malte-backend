from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    # this viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    queryset = Product.objects.all() 
    # here we specify the serializer class that should be used for validating and deserializing input, and for serializing output.
    serializer_class = ProductSerializer