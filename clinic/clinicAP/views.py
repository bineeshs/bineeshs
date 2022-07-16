from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from clinicAP.models import Booked


def Home(request):
    return render (request,'index.html')
# def demo2(request):
#     return render (request,'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        Email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return  redirect("register")
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email already taken")
                return  redirect("register")
            else:
                user = User.objects.create_user(email=Email,username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            print("password not matching")
            return redirect('register')
        return redirect('/')

    return  render(request, "register.html")


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=Username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('appo')
        else:
            messages.info(request,"Username or password is incorrect")
            return redirect('login')

    return render(request,"login.html")

def booking(request):

        if request.method == 'POST':
            username = request.POST['name']
            contact = request.POST['contact']
            date = request.POST['date']
            book = Booked(name=username, contact=contact, date=date)
            book.save();
            messages.info(request, "Booking completed")
            print("Booking completed")

        return render(request,'booking.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def appo(request):

    return render(request, 'appoinment.html')

