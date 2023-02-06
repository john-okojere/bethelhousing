from django.db import models
import uuid
from users.models import CustomUser as User

class Messagechats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name="sender", null=True)
    reciever = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reciever", null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message)
