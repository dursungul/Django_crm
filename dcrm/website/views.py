from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home_req(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "you have been logged")
            return redirect('home')
        else:
            messages.success(request,"There was an error")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})


def index_req(request):
    return render(request,'index.html',{})
   