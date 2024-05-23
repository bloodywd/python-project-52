from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('', views.TaskIndexView.as_view(), name='tasks'),
    path('create/', views.TaskFormCreateView.as_view(), name='create_task'),
    path('<int:pk>/update/', views.TaskFormUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.TaskFormDeleteView.as_view(), name='delete_task'),
    path('<int:pk>/', views.TaskView.as_view(), name='view_task'),
]
