from django import forms
from .models import Client, Project, Task

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date']