from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        if request.POST['username'] and request.POST["password1"]:
            if request.POST["password1"]==request.POST["password2"]:
                try:
                    user=User.objects.get(username=request.POST['username'])
                    return render(request,'account/signup.html',{'error':'User Already Exists'})
                except User.DoesNotExist:
                    user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    return redirect('login')
            else:
                return render(request,'account/signup.html',{'error':'Password Not Matched'})
        else:
            return render(request,'account/signup.html',{'error':'Fill All Fields'})
    else:
        return render(request,'account/signup.html')



def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            return render(request,'product/main.html')
        else:
            return render(request,'account/login.html' , {'error':'User Name Or Password Is Incorrect'})
    else:
        return render(request,'account/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
        
    
    