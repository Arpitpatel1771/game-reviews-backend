from django.db import models
import uuid
from backend.constants import TASK_STATUSES


class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    title = models.CharField(max_length=500)
    description = models.TextField()
    status = models.CharField(max_length=250, choices=TASK_STATUSES, default=TASK_STATUSES[0][0])

    def __str__(self):
        return f"{self.id}: {self.title} ({self.get_status_display()})"
    