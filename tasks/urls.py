from django.urls import path, include
from . views import *

urlpatterns = [
    path("",task_list, name='task_list'),
    path("add/",add_task, name="add_task"),
    path("view/<int:id>/", view_task, name="view_task"),
    path("edit/<int:id>/", edit_task, name="edit_task"),
    path("delete/<int:id>/",delete_task, name="delete_task"),
]