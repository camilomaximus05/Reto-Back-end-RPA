from rest_framework import routers
from Registro_de_fronteras.controllers.LbcController import LbcViewSet

router = routers.DefaultRouter()

router.register(r'api/registro_de_fronteras/lbc', LbcViewSet,'lbc');

urlpatterns = router.urls