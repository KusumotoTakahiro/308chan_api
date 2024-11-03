from rest_framework import routers
from .views import RoomViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'room', RoomViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
]

urlpatterns += router.urls