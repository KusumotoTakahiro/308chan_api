from rest_framework import viewsets
from .models import Room, Comment
from .serializer import RoomSerializer, CommentSerializer


# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer