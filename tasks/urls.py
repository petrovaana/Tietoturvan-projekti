from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="list"),
    path("create/", views.create_task, name="create"),
    path("users/<int:user_id>/", views.user_task_list, name="user_list"),
    path("<int:task_id>/delete/", views.delete_task, name="delete"),
]
