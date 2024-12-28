from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('list/', views.teachers_list, name='list'),
    path('add/', views.teacher_add, name='teacher-add'),
]