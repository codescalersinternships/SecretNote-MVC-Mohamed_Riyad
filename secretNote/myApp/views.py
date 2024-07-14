from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Note

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, NoteForm
from .forms import SignInForm


@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'myApp/create_note.html', {'form': form})


def home(request):
    return render(request, 'myApp/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = SignUpForm()

    return render(request, 'myApp/signup.html', {'form': form})


def signin(request):
    form = SignInForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        print("zzz")
        print(form.errors)

    return render(request, 'myApp/signin.html', {'form': form})


def note(request, note_id):
    my_note = get_object_or_404(Note, pk=note_id)
    if my_note.view_count == my_note.max_count:
        raise Http404("Note has expired")
    my_note.view_count = my_note.view_count + 1
    my_note.save()
    return render(request, "myApp/note.html", {"noteContent": my_note.content})
