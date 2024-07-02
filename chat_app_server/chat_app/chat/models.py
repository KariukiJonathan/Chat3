from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatParticipantsChannel(models.Model):
    channel = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.channel)


class ChatRoom(models.Model):
    name = models.CharField(max_length=256)

    # Store the last message and the user who sent it
    last_message = models.CharField(max_length=2048, null=True)
    last_sent_user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Messages(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.user.username}: {self.content[:50]}...'


class ChatRoomParticipants(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    room = models.ForeignKey(ChatRoom, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.username} in {self.room.name}'
