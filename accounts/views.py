from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import request
from . forms import UserLoginForm
# Create your views here.
### 
def userLogin(request):
    form = UserLoginForm()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = UserLoginForm(request.POST)
        user = authenticate(username=username,password=password)
        
        if user is not None: 
            login(request,user)   
            return redirect('/')

    context = {'form':form}
    return render(request,'accounts/login.html', context)

def userLogOut(request):
    logout(request)
    return redirect('/')