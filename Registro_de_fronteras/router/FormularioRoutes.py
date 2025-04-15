from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..controllers.FormularioController import FormularioFronteraViewSet


router = DefaultRouter()
router.register(r'registro_frontera', FormularioFronteraViewSet, basename='registro_frontera')


urlpatterns = router.urls