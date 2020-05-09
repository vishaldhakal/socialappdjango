from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from post.views import index
from .models import Profile,friendRequest

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username = username).exists():
            return HttpResponse("User Already Exists")
        else:
            if User.objects.filter(email = email).exists():
                return HttpResponse("Email Already Exists")
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                return render(request,'registration/login.html')

    return render(request,'registration/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')

    else:
        return render(request, 'registration/login.html')

def logout(request):
    id = request.user.id
    usersobj = User.objects.get(pk=id)
    auth.logout(request)
    return redirect('register')

def addfriendreq(request,id):
    receiver = Profile.objects.get(pk=id)
    sender = Profile.objects.get(id=request.user.id)
    frend = friendRequest(frommm=sender,to=receiver)
    frend.save()
    context = {'rec':receiver,'sen':sender}
    return redirect('users')

def deletefriendreq(request,id):
    receiver = Profile.objects.get(id=id)
    sender = Profile.objects.get(user=request.user)
    context = {'rec':receiver,'sen':sender}
    return render(request,'registration/dashboard.html',context)

def acceptfriendreq(request,id):
    receiver = Profile.objects.get(id=id)
    sender = Profile.objects.get(user=request.user)
    context = {'rec':receiver,'sen':sender}
    return render(request,'registration/dashboard.html',context)