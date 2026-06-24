from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls