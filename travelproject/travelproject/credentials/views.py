from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(reguest):
    if reguest.method=='POST':
        First_name=reguest.POST['First_Name']
        last_name = reguest.POST['Last_Name']
        Email = reguest.POST['Email']
        number = reguest.POST['Mobile Number']
        username = reguest.POST['Username']
        password = reguest.POST['password']
        cpassword = reguest.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(reguest,"username already taken")
                return  redirect("register")
            elif User.objects.filter(email=Email).exists():
                messages.info(reguest,"Email already taken")
                return  redirect("register")
            else:
                user= User.objects.create_user(first_name=First_name,last_name=last_name,email=Email,username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(reguest,"password not matching")
            print("password not matching")
            return redirect('register')
        return redirect('/')

    return  render(reguest, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
