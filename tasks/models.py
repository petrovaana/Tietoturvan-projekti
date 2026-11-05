from django.conf import settings
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
