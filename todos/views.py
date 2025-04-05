# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404 # Import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST # To ensure views only accept POST requests
from django.http import HttpResponseForbidden # To return if user doesn't own the item

from .models import TodoItem
from .forms import TodoForm

# --- Authentication Views ---
def signup(request):
    # ... (keep signup view as is) ...
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# --- Home/Todo View ---
def home(request):
    # ... (keep home view as is) ...
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        if request.method == 'POST':
            # This POST handling is only for ADDING todos via the main form
            form = TodoForm(request.POST)
            if form.is_valid():
                todo_item = form.save(commit=False)
                todo_item.user = request.user
                todo_item.save()
                return redirect('home')
            # If invalid, fall through to render with the invalid form
        else: # GET request
            form = TodoForm() # Create empty form for adding

        user_todos = TodoItem.objects.filter(user=request.user).order_by('created_at')
        context = {
            'todo_list': user_todos,
            'add_todo_form': form, # Pass the form instance (empty or invalid)
        }
        return render(request, 'home.html', context)


# --- Update and Delete Views ---

@login_required # Ensure user is logged in
@require_POST # Ensure this view only accepts POST requests
def update_todo_status(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)

    # Check if the logged-in user owns this todo item
    if todo.user != request.user:
        return HttpResponseForbidden("You do not have permission to update this item.")

    # Simple toggle logic: If Done -> Pending, otherwise -> Done
    if todo.status == 'DONE':
        todo.status = 'PENDING'
    else:
        # Consider adding 'IN_PROGRESS' later if needed
        todo.status = 'DONE'

    todo.save()
    return redirect('home') # Redirect back to the homepage

@login_required # Ensure user is logged in
@require_POST # Ensure this view only accepts POST requests
def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)

    # Check if the logged-in user owns this todo item
    if todo.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this item.")

    todo.delete()
    return redirect('home') # Redirect back to the homepage