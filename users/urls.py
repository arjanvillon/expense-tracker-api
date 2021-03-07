from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knox import views as knox_views

from .views import (LoginApiView, RegisterApiView, UserApiView, WalletViewSet,)

router = DefaultRouter()
router.register("wallet", WalletViewSet, basename="Wallet")

urlpatterns = [
    path("register", RegisterApiView.as_view()),
    path("login", LoginApiView.as_view()),
    path("logout", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("", UserApiView.as_view()),
    path("", include("knox.urls")),
    path("", include(router.urls)),
]
