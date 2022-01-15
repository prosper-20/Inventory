from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, your account has been created successfully!")
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }

    return render(request, 'users/register.html', context)

# Create your views here.