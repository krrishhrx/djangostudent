from django.shortcuts import render, redirect
from school_app.models import Student
from school_app.forms import StudentForm

# Create your views here.

def ind(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/register')
    return render(request,'index.html')

def register(request):
    student = Student.objects.all()
    return render(request,'register.html',{'student': student })

def edit(request, id):
    student = Student.objects.get(id =id)
    return render(request, 'edit.html', {'student': student } )

def update(request, id):
    student = Student.objects.get(id = id)
    form =StudentForm(request.POST, instance = student )
    if form.is_valid():
        form.save()
        return redirect('/register')
    return render(request, 'register.html', {'student': student })

def trash(request, id):
    student = Student.objects.get(id = id)
    student.delete()
    return redirect('/register')