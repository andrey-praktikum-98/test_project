from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import FoodCategoryViewSet

app_name = 'api'

router = SimpleRouter()
router.register('foods', FoodCategoryViewSet)
router.register('foods', FoodCategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
