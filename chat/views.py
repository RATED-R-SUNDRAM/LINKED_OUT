from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from home.models import UserDetails


def home(request):
    """Shows chat app home page"""
    return render(request, "chat/home.html")


def room(request, room):
    """Shows chatroom page
    
    Args:
        request: Contains username
    
    Context:
        model: :model:`models.UserDetails`,
        username: username,
        room: room id,
        room_details: dict with room details
        usr: User details
    
    Templates:
        :template:`chat/room.html`
    """
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    usr = UserDetails.objects.all()
    return render(
        request,
        "chat/room.html",
        {"username": username, "room": room, "room_details": room_details, "usr": usr},
    )


def checkview(request):
    """Returns room if it exists else creates it
    
    Args:
        request: Contains room(room_name), username
    
    Redirects to /<room_id>
    """
    room = request.POST["room_name"]
    username = request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect("/" + room + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/" + room + "/?username=" + username)


def send(request):
    """Sends message 

    Args:
        request: contains message, username, room_id
    """
    message = request.POST["message"]
    username = request.user
    room_id = request.POST["room_id"]
    usr = UserDetails.objects.get(username=username)
    name = usr.username
    new_message = Message.objects.create(
        value=message, user=usr, room=room_id, name=name
    )
    new_message.save()
    return HttpResponse("Message sent successfully")


def getMessages(request, room):
    """Returns all messages sent in a room
    
    Args:
        request:  Contains room name(room_id)

    Context:
        messages: all messages sent in a room  
    """
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.name)
    return JsonResponse({"messages": list(messages.values())})
