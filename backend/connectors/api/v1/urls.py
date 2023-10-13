from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TrelloViewSet, TestConnectorViewSet

router = DefaultRouter()
router.register("trello", TrelloViewSet, basename="trello")
router.register("testconnector", TestConnectorViewSet, basename="testconnector")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
