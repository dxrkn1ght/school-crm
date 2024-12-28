from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('list/', views.students_list, name='list'),
    path('add/', views.student_add, name='student-add'),
    path('detail/', views.student_detail, name='detail'),
]