from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid username and/or password')
            return redirect('login')

    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['repass']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save();
                messages.info(request,'user created')
                return redirect('login')
                

        else:
            messages.info(request,'password not matching...')
            return redirect('register.html')
        return redirect("/")
    
    else:
        return render(request,'register.html')





