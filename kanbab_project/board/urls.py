from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('board/<int:board_id>/view/', views.get_board_view),
    path('task/<int:task_id>/move/', views.move_task),
    path('column/<int:column_id>/reorder/', views.reorder_tasks),
]
