import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models.message import Message
from chat.models.room import Room
from users.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    """Consumer for handling WebSocket connections in the chat room."""

    async def connect(self):
        """
        Called when the WebSocket is handshaking
        as part of the connection process.
        """
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """Called when the WebSocket closes for any reason."""
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        """Called when the server receives a message from WebSocket."""
        data = json.loads(text_data)
        message_content = data["message"]
        email = data["email"]
        room = data["room"]

        await self.save_message(email, room, message_content)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message_content,
                "email": email
            },
        )

    async def chat_message(self, event):
        """Called when message is received from room group."""
        message = event["message"]
        email = event["email"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "email": email,
                }
            )
        )

    @sync_to_async
    def save_message(self, email, room, message_content):
        """Save a new message to the database."""
        user = User.objects.get(email=email)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message_content)
