from django.shortcuts import get_object_or_404, render
from .models import Messagechats
from users.models import CustomUser as User
from django.http import HttpResponse, JsonResponse
from itertools import chain


def sendmessage(request, pk):
    sender = request.user
    reciever = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        message = request.POST.get('message')
        chat = Messagechats.objects.create(sender=sender, reciever=reciever ,message=message)
        chat.save()
        return HttpResponse('')
    return JsonResponse({'post':'false'})

def messages(request, pk):
    person = get_object_or_404(User, pk= pk)
    sender_messages = Messagechats.objects.filter(sender=person, reciever=request.user).values()
    receiver_messages = Messagechats.objects.filter(sender=request.user, reciever=person).values()
    Messagechats.objects.filter(sender=person, reciever=request.user).update(is_read = True)
    data = list(chain(sender_messages, receiver_messages))

    return JsonResponse({"messages" :data})

def get_unread_messages(request):
    data = Messagechats.objects.filter(reciever=request.user, is_read=False).count()
    return JsonResponse({"unread_messages": data})


def get_someone_unread_messages(request, pk):
    person = get_object_or_404(User, pk= pk)
    data = Messagechats.objects.filter(reciever=request.user, sender=person ,is_read=False).count()
    return JsonResponse({"unread_messages": data})