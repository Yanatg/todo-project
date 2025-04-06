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


# todos/views.py (Examples of refactored parts)

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied

from . import services # Import the service module
from .forms import TodoForm
from .models import TodoItem # May still be needed for DoesNotExist exception

# --- Home/Todo View ---
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                try:
                    services.create_todo(
                        user=request.user,
                        title=form.cleaned_data['title'],
                        description=form.cleaned_data['description']
                    )
                    return redirect('home')
                except ValueError as e: # Example: Catch specific service errors
                    form.add_error(None, str(e)) # Add non-field error
                # Let invalid form fall through
        else: # GET request
            form = TodoForm()

        user_todos = services.get_todos_for_user(user=request.user)
        context = { 'todo_list': user_todos, 'add_todo_form': form }
        return render(request, 'home.html', context)

# --- Update and Delete Views ---
@login_required
@require_POST
def update_todo_status(request, todo_id):
    try:
        services.update_todo_status(user=request.user, todo_id=todo_id)
    except TodoItem.DoesNotExist:
        raise Http404("Todo item not found")
    except PermissionDenied as e:
        return HttpResponseForbidden(str(e))
    # Handle other potential service exceptions if needed
    return redirect('home')

@login_required
@require_POST
def delete_todo(request, todo_id):
    try:
        services.delete_todo(user=request.user, todo_id=todo_id)
    except TodoItem.DoesNotExist:
        raise Http404("Todo item not found")
    except PermissionDenied as e:
        return HttpResponseForbidden(str(e))
    # Handle other potential service exceptions if needed
    return redirect('home')

# Keep signup view as is (uses UserCreationForm which handles its own logic)
# ...