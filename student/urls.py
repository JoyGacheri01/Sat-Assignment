from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('insert/',views.insert, name="insert"),
    path('insert_data/', views.insert_data, name="insert_data"),
    path('view/', views.view, name="view"),
    path('details/', views.details, name="detail"),
    path('UpdateStud/', views.UpdateStud, name="UpdateStud"),
    path('details/<id>/', views.get_student, name='details'),
    path('update_student/<id>/', views.update_student, name='update_student'),
    path('delete_student/<id>/', views.delete_student, name='delete_student'),
]