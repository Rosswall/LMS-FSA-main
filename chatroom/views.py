from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from django.contrib.auth.decorators import login_required
from .forms import ChatRoomForm

app_name = 'chatroom'

@login_required
def chatrooms(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chatrooms.html', {'rooms': rooms})

@login_required
def room(request, room_name):
    room = ChatRoom.objects.get(name=room_name)
    messages = room.messages.all()
    return render(request, 'room.html', {'room': room, 'messages': messages})

@login_required
def send_message(request, room_name):
    if request.method == 'POST':
        room = ChatRoom.objects.get(name=room_name)
        message = Message.objects.create(
            room=room,
            user=request.user,
            content=request.POST['content']
        )
        return redirect('room', room_name=room_name)
    
@login_required
def create_chatroom(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chatrooms')  # Redirect to the chatrooms list
    else:
        form = ChatRoomForm()
    
    return render(request, 'create_chatroom.html', {'form': form})