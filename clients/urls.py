from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.client_list, name='client_list'),
    path('add/', views.client_create, name='client_create'),
    path('client/<int:client_id>/edit/', views.client_update, name='client_update'),
    path('client/<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('client/<int:client_id>/projects/', views.project_list, name='project_list'),
    path('client/<int:client_id>/projects/add/', views.project_create, name='project_create'),
    path('project/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('project/<int:project_id>/tasks/add/', views.task_create, name='task_create'),
    path('task/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='clients/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
