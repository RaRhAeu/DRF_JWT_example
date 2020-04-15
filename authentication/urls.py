from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ObtainTokenPairWithData, CustomUserCreate, DummyHelloWorldView

urlpatterns = [
    path('token/obtain/', ObtainTokenPairWithData.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name='create_user'),
    path('hello/', DummyHelloWorldView.as_view(), name='hello_world')
]