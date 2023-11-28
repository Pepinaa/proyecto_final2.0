from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreatePollForm
from .models import Poll
from .models import Vote
from django.contrib import messages
from datetime import datetime



def home(request):
    today = datetime.now()
    current_month = today.month
    current_year = today.year

    polls = Poll.objects.filter(
        created_at__year=current_year, created_at__month=current_month
    )

    context = {
        'polls': polls,
        'total_polls_this_month': polls.count()  # Contador para mostrar en la plantilla
    }

    return render(request, 'poll/home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            option_one = "Sí"
            option_two = "No"
            poll = Poll.objects.create(
                question=question,
                option_one=option_one,
                option_two=option_two
            )
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    user = request.user  


    if Vote.objects.filter(poll=poll, user=user).exists():
        messages.warning(request, 'Ya has votado en esta encuesta.')
        return redirect('results', poll_id=poll.id)

    if request.method == 'POST':
        selected_option = request.POST.get('poll', None)
        
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        else:
            return render(request, 'poll/vote.html', {'poll': poll, 'error_message': 'Selecciona una opción válida'})

        poll.save()

        Vote.objects.create(poll=poll, user=user)

        return redirect('results', poll_id=poll.id)

    context = {'poll': poll}
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)