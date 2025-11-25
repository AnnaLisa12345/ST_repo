from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SinkholeViewSet

router = DefaultRouter()
router.register(r'sinkholes', SinkholeViewSet, basename='sinkhole')

urlpatterns = [
    path('', include(router.urls)),
]
