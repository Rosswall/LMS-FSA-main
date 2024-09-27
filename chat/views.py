from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Chat, User

def user_list_view(request):
    # List all users
    users = User.objects.all()
    return render(request, 'chat/user_list.html', {'users': users})

def chat_view(request, username):
    # Get the receiver user (selected user)
    selected_user = get_object_or_404(User, username=username)

    # Get the sender from the query string, or default to None if not provided
    sender_username = request.GET.get('sender', None)

    # Handle the case where no sender is provided
    if not sender_username:
        return redirect('chat:user_list')  # Adjust as needed to handle missing sender

    # Fetch the sender user from the database
    sender = get_object_or_404(User, username=sender_username)

    # Fetch messages between the selected sender and receiver
    messages = Chat.objects.filter(
        (Q(sender=sender) & Q(receiver=selected_user)) |
        (Q(sender=selected_user) & Q(receiver=sender))
    ).order_by('timestamp')

    if request.method == "POST":
        message_text = request.POST.get('message', '')
        if sender and selected_user and message_text:
            Chat.objects.create(sender=sender, receiver=selected_user, message=message_text)
            return redirect('chat:chat_view', username=selected_user.username)

    # Fetch a list of users for selection
    users = User.objects.exclude(username=sender.username)

    context = {
        'selected_user': selected_user,
        'messages': messages,
        'sender': sender,
        'users': users,
    }

    return render(request, 'chat/chat_view.html', context)




# def send_message_form(request):
#     if request.method == "POST":
#         recipient_username = request.POST.get('recipient')
#         message_text = request.POST.get('message')
#         sender_username = request.POST.get('sender')  # Assume sender is passed from the form
#         recipient = get_object_or_404(User, username=recipient_username)
#         sender = get_object_or_404(User, username=sender_username)
#         if recipient and sender and message_text:
#             Chat.objects.create(sender=sender, receiver=recipient, message=message_text)
#             return redirect('chat:chat_view', username=recipient_username)  # Corrected redirect
#     users = User.objects.all()
#     context = {
#         'users': users
#     }
#     return render(request, 'chat/send_message_form.html', context)