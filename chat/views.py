from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from home.models import userDetails
# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    usr=userDetails.objects.all()
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'usr':usr
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.user
    room_id = request.POST['room_id']
    usr=userDetails.objects.get(username=username)
    name=usr.username
    new_message = Message.objects.create(value=message, user=usr, room=room_id,name=name)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.name)
    return JsonResponse({"messages":list(messages.values())})