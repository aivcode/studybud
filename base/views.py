from django.shortcuts import render
from .models import Room
from .forms import RoomForm


# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        # https://youtu.be/PtQiiknWUcI?t=6619
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
