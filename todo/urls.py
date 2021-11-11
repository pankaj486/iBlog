from django.urls import path
from . import views



urlpatterns = [
    path('todo/', views.create_todo, name='todo'),
    path('todo/<int:id>/', views.edit_todo, name='edit_todo'),
    path('todo/remove/<int:id>/', views.remove, name='remove'),

]
