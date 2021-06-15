from math import ceil
from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
import rooms


def all_rooms(request):
    page = request.GET.get("page")
    rooms = models.Room.objects.all()
    paginator = Paginator(rooms, 10, orphans=5)
    pages = paginator.get_page(page)

    return render(
        request,
        "rooms/home.html",
        context={
            "pages": pages,
        },
    )
