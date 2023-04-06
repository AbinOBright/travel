from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Not Registered")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first = request.POST['first_name']
        last = request.POST['last_name']
        mail = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST.get('password1')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first,last_name=last,email=mail)

                user.save();

                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')