from django.http import HttpResponse
from django.shortcuts import render

from chat.models.message import Message
from chat.models.room import Room
from chat.tokenizer import create_token


def index(request) -> HttpResponse:
    """Render page with all rooms."""
    rooms = Room.objects.all()
    return render(request, "chat/index.html", {"rooms": rooms})


def room(request, slug) -> HttpResponse:
    """Render the chat room page."""
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    token = create_token(request.user.id)["access_token"]
    context: dict = {
        "room": room,
        "messages": messages,
        "user_email": request.user.email,
        "token": token,
    }
    return render(request, "chat/room.html", context)
