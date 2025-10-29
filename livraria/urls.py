from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import LivroViewSet

router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
