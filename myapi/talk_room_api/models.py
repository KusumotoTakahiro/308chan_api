from django.db import models
import uuid


class Room(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100)
  description = models.TextField()


class Comment(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  body = models.TextField()
  talker = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
