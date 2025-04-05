"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# todoproject/urls.py

from django.contrib import admin
from django.urls import path, include # Make sure include is imported
from todos import views as todos_views # Import views from your todos app

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include Django's built-in authentication URLs (for login, logout, password management)
    # This line provides URLs like /accounts/login/, /accounts/logout/, etc.
    path('accounts/', include('django.contrib.auth.urls')),

    # URL for our custom signup view
    path('accounts/signup/', todos_views.signup, name='signup'),

    # Add a basic home page URL (we'll create the view next)
    path('', todos_views.home, name='home'),

    # Add other app-specific URLs later (e.g., for listing/adding todos)
    # path('todos/', include('todos.urls')), # Example for later
]