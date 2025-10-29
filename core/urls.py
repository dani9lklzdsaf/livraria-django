from django.urls import path, include
from rest_framework import routers
from .views import LivroViewSet

router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
