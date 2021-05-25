from django.shortcuts import render, redirect,HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .forms import *

# Create your views here.
def home(request):
    return render(request,'LogInOut/home.html')

class SignUpView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request,'LogInOut/signup.html',{'form':fm,})

    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save() #user = fm.save()
            # user.set_password(user.password) #for more encryption techniques.
            #user.save() 
            messages.success(request,'Congratulation! Registration successful.')
            return redirect('/signup')
        else:
            return render(request,'LogInOut/signup.html',{'form':fm,})


class LoginView(View):
    def get(self,request):
        fm = LoginForm()
        return render(request,'LogInOut/login.html',{'form':fm})

    def post(self,request):
        fm = LoginForm(request, data=request.POST)

        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Logged in Successfully!!')
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'username or password not correct')
                return redirect('LogInOut/login.html')
        else:
            return render(request,'LogInOut/login.html',{'form':fm})
