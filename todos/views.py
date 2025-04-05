from django.shortcuts import render

# Create your views here.
# todos/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Django's built-in signup form
from django.contrib.auth import login # To log the user in after signup

# Keep your TodoItem model import if it's there
from .models import TodoItem

# --- Authentication Views ---

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the new user
            login(request, user) # Log the user in
            return redirect('home') # Redirect to home page after signup
    else: # If GET request
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# --- Basic Site Views ---

def home(request):
    return render(request, 'home.html')

# --- Todo Views (Add these later) ---
# def todo_list(request):
#     pass
# def add_todo(request):
#     pass
# ... etc ...