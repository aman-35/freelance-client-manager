from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Client, Project, Task
from .forms import ClientForm, ProjectForm, TaskForm


def home(request):
    if request.user.is_authenticated:
        return redirect('client_list')
    return render(request, 'clients/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('client_list')
    else:
        form = UserCreationForm()
    return render(request, 'clients/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def client_list(request):
    clients = Client.objects.filter(owner=request.user)
    return render(request, 'clients/client_list.html', {'clients': clients})


@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.owner = request.user
            client.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})


@login_required
def project_list(request, client_id):
    client = get_object_or_404(Client, id=client_id, owner=request.user)
    projects = client.projects.all()
    return render(request, 'clients/project_list.html', {'client': client, 'projects': projects})


@login_required
def project_create(request, client_id):
    client = get_object_or_404(Client, id=client_id, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = client
            project.save()
            return redirect('project_list', client_id=client.id)
    else:
        form = ProjectForm()
    return render(request, 'clients/project_form.html', {'form': form, 'client': client})


@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id, client__owner=request.user)
    tasks = project.tasks.all()
    return render(request, 'clients/task_list.html', {'project': project, 'tasks': tasks})


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, client__owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'clients/task_form.html', {'form': form, 'project': project})


@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__client__owner=request.user)
    task.completed = not task.completed
    task.save()


@login_required
def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id, owner=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form, 'client': client})


@login_required
def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id, owner=request.user)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})
    return redirect('task_list', project_id=task.project.id)