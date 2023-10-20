from django.db import models
from user_registration.models import UserProfile

class Chat(models.Model):
    participants = models.ManyToManyField(UserProfile, related_name='chats')


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    product_title = models.CharField(max_length=200, null=False, blank=False)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="Sender")
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="Receiver")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Reply(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="Author")
    created_at = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']





