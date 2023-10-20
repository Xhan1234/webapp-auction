from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, Reply, Chat
from .forms import MessageForm, ReplyForm
from django.contrib.auth.decorators import login_required
from user_registration.models import UserProfile
from datetime import datetime
from django.db.models import Q
from django.http import Http404, HttpResponseForbidden
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url='/log-in/')
def index(request):

    inbox = 'Inbox'
    outbox = 'Onbox'

    # Retrieve messages where the current user is either the sender or the recipient
    messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).order_by('-created_at')

    return render(request, 'chat/index.html', {
        'inbox': inbox,
        'outbox': outbox,
        'messages': messages,

    })


@login_required(login_url='/log-in/')
def send_message(request, author_id, product_title):
    author = get_object_or_404(UserProfile, id=author_id)
    author_username = author.username

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create a new message and set its attributes
            message = Message()
            message.product_title = form.cleaned_data['product_title']
            message.subject = form.cleaned_data['subject']
            message.message = form.cleaned_data['message']
            message.sender = request.user
            message.recipient = author
            message.created_at = datetime.now()
            message.save()

            # Create a new chat associated with the message
            chat = Chat.objects.create()
            chat.participants.add(request.user, author)  # Add participants to the chat

            # Associate the chat with the message and save it
            message.chat = chat
            message.save()

            return redirect('read_message', chat_id=chat.id)

    else:
        form = MessageForm()

    return render(request, 'temp-files/message_1/index.html', {
        'title': 'Send Message',
        'form': form,
        'author_username': author_username,
        'product_title': product_title
    })




@login_required(login_url='/log-in/')
def read_message(request, chat_id):
    title = "Read message"

    # Retrieve the chats related to the chat_id using get_object_or_404
    chats = get_object_or_404(Chat, id=chat_id)

    # Check if the user is a participant in this chat
    can_reply = chats.participants.filter(id=request.user.id).exists()

    print(f"can_reply: {can_reply}")
    print(f"chats: {chats}")
    print(f"chats.participants: {chats.participants.all()}")
    print(f"request.user: {request.user}")
    participants = chats.participants.all()
    if request.user not in participants:
        # If the user is not a participant, handle it accordingly
        return HttpResponseForbidden("You do not have permission to access this chat.")

    # Initialize form variable
    form = ReplyForm()

    if not can_reply:
        # If the user is not a participant, handle it accordingly, e.g., return an error message or redirect
        messages = None  # Initialize messages as None
        replies = None  # Initialize replies as None
    else:
        # Retrieve messages related to the chat, ordered by created_at
        messages = chats.message_set.all().order_by('created_at')
        replies = Reply.objects.filter(message=messages.first()).order_by('created_at')

    print(f"messages: {messages}")
    print(f"replies: {replies}")

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user  # Set the author
            reply.message = messages.first()
            reply_to_id = request.POST.get('reply_to_id')
            if reply_to_id:
                try:
                    reply_to = Reply.objects.get(id=reply_to_id)
                    reply.reply_to = reply_to
                except Reply.DoesNotExist:
                    raise Http404("Reply not found")
            else:
                reply.reply_to = None
            reply.save()
            form = ReplyForm()  # Clear the form after a successful reply

            return HttpResponseRedirect(request.path)  # This line redirects to the current page (PRG pattern)
        else:
            print(form.errors)

    return render(request, 'chat/read.html', {
        'title': title,
        'chats': chats,
        'messages': messages,
        'replies': replies,
        'form': form,  # Include the form in the context
        'can_reply': can_reply
    })