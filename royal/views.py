from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



# Create your views here

def home(request):
    return render(request,'home.html')

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
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save();
                print('user created')

        else:
            print('password not matching...')
            return redirect('/')
    
    else:
        return render(request,'register.html')

def logout_request(request):
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def car_model(request):
    return render(request,'car_model.html')

