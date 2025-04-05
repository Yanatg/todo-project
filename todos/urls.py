# todos/urls.py
from django.urls import path
from . import views # Import views from the current directory (todos app)

urlpatterns = [
    # Home page (displays list and add form)
    path('', views.home, name='home'),

    # Signup (moved here from project urls)
    path('signup/', views.signup, name='signup'), # Ensure name consistency if used elsewhere

    # Update status URL - expects an integer (todo_id)
    path('update/<int:todo_id>/', views.update_todo_status, name='update_todo_status'),

    # Delete URL - expects an integer (todo_id)
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]