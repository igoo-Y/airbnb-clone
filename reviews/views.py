from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.conf import path
from django.contrib import messages
from rooms import models as room_models
from . import forms


def create_review(request, room):
    print(request.method)
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        room = room_models.Room.objects.get_or_none(pk=room)
        if not room:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.room = room
            review.user = request.user
            review.save()
            messages.success(request, "Room Reviewed!")
            return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))
