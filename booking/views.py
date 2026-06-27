from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from datetime import date
from .models import Room


from django.db.models import Q

def index(request):
    return render(request, "booking/index.html")


def search(request):
    rooms = Room.objects.all()

    name = request.GET.get("name")
    places = request.GET.get("places")

    if name:
        rooms = rooms.filter(name__icontains=name)

    if places:
        rooms = rooms.filter(capacity__gte=places)

    return render(
        request,
        "booking/search.html",
        {
            "rooms": rooms,
        },
    )


def detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    return render(
        request,
        "booking/detail.html",
        {
            "room": room,
        },
    )

def book(request, room_id: int):
    return HttpResponse(f"Booked {room_id}")
