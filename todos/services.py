# todos/services.py

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import TodoItem, User # Assuming User model is relevant

def create_todo(user: User, title: str, description: str | None = None) -> TodoItem:
    """
    Creates a new TodoItem for the given user.
    """
    if not title:
        raise ValueError("Title cannot be empty.") # Example business rule

    todo = TodoItem.objects.create(
        user=user,
        title=title,
        description=description
        # Status defaults to 'PENDING' in the model
    )
    return todo

def get_todos_for_user(user: User): # -> QuerySet[TodoItem]: (Using type hints)
    """
    Retrieves all non-deleted TodoItems for a specific user.
    """
    return TodoItem.objects.filter(user=user).order_by('created_at') # Or default order

def update_todo_status(user: User, todo_id: int) -> TodoItem:
    """
    Toggles the status of a specific TodoItem if the user owns it.
    Raises PermissionDenied if user does not own the item.
    Raises TodoItem.DoesNotExist if item not found.
    """
    todo = get_object_or_404(TodoItem, id=todo_id)

    if todo.user != user:
        raise PermissionDenied("User does not have permission to update this item.")

    # Toggle logic
    if todo.status == 'DONE':
        todo.status = 'PENDING'
    else:
        todo.status = 'DONE'

    todo.save(update_fields=['status', 'updated_at']) # Be specific about updated fields
    return todo

def delete_todo(user: User, todo_id: int) -> bool:
    """
    Deletes a specific TodoItem if the user owns it.
    Returns True if deleted, False otherwise (though raising errors is often better).
    Raises PermissionDenied if user does not own the item.
    Raises TodoItem.DoesNotExist if item not found.
    """
    todo = get_object_or_404(TodoItem, id=todo_id)

    if todo.user != user:
        raise PermissionDenied("User does not have permission to delete this item.")

    todo.delete()
    return True