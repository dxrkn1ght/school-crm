from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('list/', views.subjects_list, name='list'),
    path('add/', views.subject_add, name='subject-add'),
]