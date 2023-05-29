from django.shortcuts import render,redirect
from student.forms import StudentForm
from student.models import Student

# Create your views here.
def index(request):
    return render(request,'student/index.html')

def add(request):
    return render(request,'student/add.html')

def edit(request,id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html',{'student':student})

def update(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'student':student})

def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show")

def save(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = StudentForm()
    return render(request,'add.html',{'form':form})
def show(request):
    students = Student.objects.all()
    return render(request,'student/show.html',{"students":students})
