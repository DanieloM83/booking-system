from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Welcome page"),
    path("search", views.search, name="Search page"),
    path("detail/<int:room_id>", views.detail, name="Booking page"),
    path("book/<int:room_id>", views.book, name="Book action"),
]
