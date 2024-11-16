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

]