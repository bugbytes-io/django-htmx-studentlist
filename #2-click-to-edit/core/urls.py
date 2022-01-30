from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='index'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),

    path('students/<int:pk>/edit', views.student_edit_form, name='student-edit-form')
]
