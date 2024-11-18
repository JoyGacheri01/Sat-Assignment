from django.urls import path
from . import views

app_name ='venture'

urlpatterns =[
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('insert_quote/', views.insert_quote, name='insert_quote'),
    path('view_quote/', views.view_quote, name='view_quote'),
    path('update_quote/<id>', views.update_quote, name='update_quote'),
    path('view_contact/', views.view_contact, name='view_contact'),
    path('insert_contact/', views.insert_contact, name='insert_contact'),
    path('update_contact/<id>', views.update_contact, name='update_contact'),
    path('delete_contact/<id>', views.delete_contact, name='delete_contact'),
    path('view/', views.view, name='view'),

]