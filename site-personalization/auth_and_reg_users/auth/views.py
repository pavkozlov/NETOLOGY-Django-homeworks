from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    context = dict()
    if request.user.is_authenticated:
        context['username'] = request.user.get_username()

    return render(
        request,
        'home.html',
        context=context
    )


def signup(request):
    data = dict()
    data['forms'] = UserCreationForm()
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')
    return render(
        request,
        'signup.html',
        context=data
    )


def thanks(request):
    return render(request, 'thanks.html')
