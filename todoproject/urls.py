# todoproject/urls.py
from django.contrib import admin
from django.urls import path, include # Make sure include is imported

# Remove the direct import of todos views here as they are now handled in todos.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include Django's built-in auth URLs (for login, logout, etc.)
    # These paths start with 'accounts/'
    path('accounts/', include('django.contrib.auth.urls')),

    # Include URLs from the 'todos' app for home, signup, update, delete
    # These paths will be relative to the root ('')
    path('', include('todos.urls')),
]