from django.db import models
from django.utils import timezone
from custom_user.models import BugUser

NEW = "NE",
IN_PROGRESS = "IP",
DONE = "DO",
INVALID = "IN"

class Ticket(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(timezone.now)
    bug = models.TextField()
    username = models.ForeignKey(BugUser, on_delete=models.CASCADE,
        related_name="user_name")

    

    TICKET_STATUS_CHOICES = [
        (NEW, "new"),
        (IN_PROGRESS, "in progress"),
        (DONE, "done"),
        (INVALID, "invalid")
    ]

    ticket_status = models.CharField(
        max_length=2,
        choices=TICKET_STATUS_CHOICES,
        default=NEW
    )

    assigned_user = models.ForeignKey(BugUser, on_delete=models.CASCADE,
        related_name="assigned")
    completed_by = models.ForeignKey(BugUser, on_delete=models.CASCADE,
        related_name="completed")

    def __str__(self):
        return f"{self.title} - {self.bug}"