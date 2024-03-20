from django.urls import path, include
from profiles_api.views import (HelloAPIView, HelloViewSet, UserProfileViewSet,
                                UserLoginApiView, UserProfileFeedViewSet)

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")
router.register("profile-viewset", UserProfileViewSet)
router.register("profile-feed", UserProfileFeedViewSet)

urlpatterns = [
    path("hello", HelloAPIView.as_view()),
    path("login", UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
