from django.urls import path
from . import views


app_name = "tasks"
urlpatterns = [
    path('', views.index, name="index"),
    path('task/new/', views.task_create, name="task_create"),
    path('task/<int:pk>/edit/', views.task_update, name="task_update"),
    path('task/<int:pk>/delete/', views.task_delete, name="task_delete"),
    path('task/<int:pk>/complete/', views.task_complete, name="task_complete"),
    path('task/<int:pk>/undo/', views.task_undo, name="task_undo"),
    path('tags/', views.tag_list, name="tag_list"),
    path('tag/new/', views.tag_create, name="tag_create"),
    path('tag/<int:pk>/edit/', views.tag_update, name="tag_update"),
    path('tag/<int:pk>/delete/', views.tag_delete, name="tag_delete"),
]
