from django.shortcuts import render, redirect
from uuid import uuid4
from django.contrib import messages
from .models import MessageData
from .helpers import terminate_link


def messageprompt(request):
    secret_link = None
    if request.method == 'POST':
        message = request.POST['secretMsg']
        secret_link = f'{uuid4()}'

        secret_generated = MessageData.objects.create(
            unique_link=secret_link,
            text=message
        )
        request.session['generated_url'] = secret_link
        return redirect('generation')
    return render(request, 'index.html')


def generation_view(request):
    if 'generated_url' in request.session.keys():
        return render(request, 'generation.html', context={
            'generated_link': request.session['generated_url']
        })
    else:
        return render('base.html')


def reveal_message(request, secret_id):
    secret = MessageData.objects.filter(unique_link=secret_id)

    if secret.exists():
        confirmed_secret = MessageData.objects.get(unique_link=secret_id)
        terminate_link(confirmed_secret.id)

        return render(request, "message.html", context={
            "secret": confirmed_secret
        })

    else:
        messages.warning(request, "Invalid URL, what are you looking for?")
        return redirect('base')
