from django.db import models

from helpers.models import TrackingModel
from authentication.models import User


class Todo(TrackingModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title