from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],email=request.POST['email'])
            auth.login(request,user)
            return redirect('home') #redirect로 바꿔
    return render(request,'signup.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home') #redirect로 바꿔
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')


@csrf_exempt
def logout(request):
    request.method = 'POST'
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home') #redirect로
    return render(request,'login.html')