from django.shortcuts import render
from django.core.mail import send_mail

from django.conf import settings
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email

        send_mail(
            message_email,
            message,
            message_name,



            ['amrouch.wadie@gmail.com'],
        )

        return render(request, 'accounts/index.html', {'message_name': message_name})

    else:
        return render(request, 'accounts/index.html', {})


