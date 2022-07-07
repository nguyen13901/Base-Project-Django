from rest_framework.routers import DefaultRouter

from api_account.views import AccountViewSet

router = DefaultRouter()
router.register("account", AccountViewSet, basename="account")


urlpatterns = router.urls
