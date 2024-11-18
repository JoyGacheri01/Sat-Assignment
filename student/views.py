from django.shortcuts import render, redirect
from django.views import View

from student.models import Student

from . serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






def index(request):
    return render(request, 'index.html')

#funtion to retrive
def get_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'details.html', {'student': student})

#updating
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        stud_name = request.POST['stud_name']
        stud_age = request.POST['stud_age']
        stud_sch = request.POST['stud_sch']
        stud_des =request.POST['stud_des']
        stud_pass = request.FILES['stud_pass']
        stud_reg = request.POST['stud_reg']

        student.title = stud_name
        student.age = stud_age
        student.school = stud_sch
        student.description = stud_des
        student.passport = stud_pass
        student.registration = stud_reg

        student.save()

        return redirect('/')

    return render(request, 'UpdateStud.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')



def insert(request):
    return render(request, 'insert.html')

def details(request):
    return render(request, 'details.html')

def UpdateStud(request):
    return render(request, 'UpdateStud.html')



def insert_data(request):
    if request.method == "POST":
        stud_name = request.POST['stud_name']
        stud_age = request.POST['stud_age']
        stud_sch = request.POST['stud_sch']
        stud_des =request.POST['stud_des']
        stud_pass = request.FILES['stud_pass']
        stud_reg = request.POST['stud_reg']

        student = Student(
            stud_name=stud_name, 
            stud_age=stud_age, 
            stud_sch=stud_sch, 
            stud_des=stud_des, 
            stud_pass = stud_pass, 
            stud_reg = stud_reg
         )
        student.save()
        return redirect('/')



    return render(request, 'insert.html')

def view(request):
    students = Student.objects.all()
    return render(request, 'view.html', {"students": students})


