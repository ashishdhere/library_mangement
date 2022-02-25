from django.shortcuts import render,redirect,HttpResponse
from .forms import Userform,Bookform
from django.contrib import messages
from .models import Book

# Create your views here.
def home(request):
    return render(request,'home.html')

def adminR(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                messages.info(request,'form is not valid')
    form = Userform
    return render(request,'adminR.html',{'form':form})

def addbook(request):
    if request.method =="POST":
        book = Bookform(request.POST)
        if book.is_valid():
            try:
                book.save()
                return redirect('showbook')
            except:
                pass
    book = Bookform()
    return render(request,'add_books.html',{'book':book})

def show(request):
    fm = Book.objects.all()
    return render(request,'show.html',{'fm':fm})

def delete(request,id):
    d = Book.objects.get(id=id)
    d.delete()
    return redirect('show')

def edit(request,id):
    book = Book.objects.get(id=id)
    return render(request,'edit.html',{'book':book})

def update(request,id):
    book= Book.objects.get(id=id)
    books = Bookform(request.POST,instance=book)
    if books.is_valid():
        books.save()
        return redirect('show')
    return render(request,'edit.html',{'book':book})

def student(request):
    book = Book.objects.all()
    return render(request,'student.html',{'book':book})
    
