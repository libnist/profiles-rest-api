from django.urls import path, include
from profiles_api.views import HelloAPIView, HelloViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")

urlpatterns = [
    path("hello", HelloAPIView.as_view()),
    path("", include(router.urls))
]
