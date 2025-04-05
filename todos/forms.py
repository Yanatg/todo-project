# todos/forms.py
from django import forms
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        # Specify fields to include in the form
        fields = ['title', 'description']
        # Optionally add widgets for styling/behavior
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional description...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter todo title...'}),
        }