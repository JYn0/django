from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Room, Message
import secrets
import json
import pusher

pusher_client = pusher.Pusher(
    app_id='key',
    key='key',
    secret='key',
    cluster='ap3',
    ssl=True
)


# Create your views here.
def index(request):
    if request.method == "POST":
        # POST이면 방만들기
        title = request.POST["room-title"]
        max_count = request.POST["room-max-count"]
        code = secrets.token_urlsafe(16)
        room = Room()
        room.title = title
        room.max_connection = max_count
        room.code = code
        room.master_id = request.user.id
        room.save()
        room.users.add(request.user)
        current_connection = len(room.users.all())
        
        context = {
            'id': room.id,
            'title': title,
            'max_connection': max_count,
            'current_connection': current_connection,
            'master': room.master.username
        }

        pusher_client.trigger('main', 'create-room', json.dumps(context))
        # pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
        # my-channel을 구독하고 있는지(채널이름), event를 발생시켰을때 my-event(이벤트이름), data
        return HttpResponse('', status=204)
    else:
        

        # POST아니면 목록 보여주기
        rooms = Room.objects.all()
        context = {
            'rooms': rooms
        }
        return render(request, 'index.html', context)


def show(request, room_id):
    if request.user.is_authenticated:
        room = Room.objects.get(id=room_id)
        room.users.add(request.user) # 현재 유저를 방에 넣기
        join_message = {
            'user': request.user.username, # 현재 방에 들어온 사람
            'contents': f'{request.user.username}님이 방에 들어왔습니다.'
        }
        pusher_client.trigger(room.code, 'chat', json.dumps(join_message))
        messages = Message.objects.filter(room_id=room.id).order_by("created_at")
        
        context = {
            # 'room': room,
            # 'messages': messages,
            'room_id': room_id,
            'current_connection': len(room.users.all())
        }
        pusher_client.trigger('main', 'update-room', json.dumps(context))

        context = {
            'room': room,
            'messages': messages,
            # 'room_id': room_id,
            # 'current_connection': len(room.users.all())
        }
        return render(request, 'show.html', context)
    else:
        return redirect('accounts:login')
    
def chat(request, room_id):
    room = Room.objects.get(id=room_id)
    message = Message()
    message.room_id = room.id
    message.contents = request.POST["contents"]
    message.user_id = request.user.id
    message.save()
    context = {
        'user': request.user.username,
        'contents': message.contents
    }
    pusher_client.trigger(room.code, 'chat', json.dumps(context))

    return HttpResponse('',status=204)

def exit(request, room_id):
    room = Room.objects.get(id=room_id)
    room.users.remove(request.user) # 현재 유저를 방에서 빼기
    exit_message = {
        'user': request.user.username, # 현재 방에 들어온 사람
        'contents': f'{request.user.username}님이 방을 나갔습니다.'
    }
    pusher_client.trigger(room.code, 'chat', json.dumps(exit_message))

    context = {
        'room_id': room_id,
        'current_connection': len(room.users.all())
    }
    pusher_client.trigger('main', 'update-room', json.dumps(context))
    return redirect('boards:index')