from django import forms
from .models import Message, Reply


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['product_title', 'subject', 'message']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text', 'reply_to')


