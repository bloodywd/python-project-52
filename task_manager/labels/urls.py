from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelIndexView.as_view(), name='labels'),
    path('create/', views.LabelFormCreateView.as_view(),
         name='create_label'),
    path('<int:pk>/update/', views.LabelFormUpdateView.as_view(),
         name='update_label'),
    path('<int:pk>/delete/', views.LabelFormDeleteView.as_view(),
         name='delete_label'),
]
