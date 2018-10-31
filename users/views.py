from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(requests):
    if requests.method == "POST":
        form = UserRegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requests, f'Account created for {username}. Now you can successfully login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(requests, 'Users/register.html', {'form': form})


@login_required
def profile(requests):
    return render(requests, 'Users/profile.html')
