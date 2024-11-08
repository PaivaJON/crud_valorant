from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapaViewSet

router = DefaultRouter()
router.register(r'mapas', MapaViewSet)

urlpatterns = [
    path('admin', include(router.urls)),
]
