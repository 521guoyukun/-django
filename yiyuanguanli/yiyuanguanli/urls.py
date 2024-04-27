from django.urls import path
from hospital_management.views import create_doctor, update_doctor, delete_doctor, view_doctor, list_doctors

urlpatterns = [
    path('create/', create_doctor, name='create_doctor'),
    path('update/<int:pk>/', update_doctor, name='update_doctor'),
    path('delete/<int:pk>/', delete_doctor, name='delete_doctor'),
    path('view/<int:pk>/', view_doctor, name='view_doctor'),
    path('', list_doctors, name='doctor_list'),
]