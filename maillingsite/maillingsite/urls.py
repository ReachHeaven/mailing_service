from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from mailling.views import ClientViewSet, MaillingViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'mailings', MaillingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
]