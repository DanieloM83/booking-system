from django.shortcuts import render
from django.http import HttpResponse

from datetime import date


# Create your views here.
def index(request):
    return HttpResponse("Hello at our hotel!")


def search(request):
    start_date: str = request.GET.get("start_date", date.today().strftime("%d-%m-%Y"))
    end_date: str = request.GET.get("end_date", date.today().strftime("%d-%m-%Y"))
    places: int = request.GET.get("places", 1)

    return HttpResponse(
        f"You are trying to search for {places} Place from {start_date} to {end_date}"
    )


def detail(request, room_id: int):
    return HttpResponse(f"Ви переглядаєте кімнату {room_id}")


def book(request, room_id: int):
    return
