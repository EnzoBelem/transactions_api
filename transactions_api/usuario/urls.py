from rest_framework import routers
from usuario.views import PessoaFisicaModelViewSet, PessoaJuridicaModelViewSet

router = routers.SimpleRouter()
router.register(r'pessoa-fisica', PessoaFisicaModelViewSet)
router.register(r'pessoa-juridica', PessoaJuridicaModelViewSet)

urlpatterns = router.urls
