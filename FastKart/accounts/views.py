from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

from accounts.forms import CustomUserRegistrationForm
from accounts.models import CustomUser

def user_signup(request):
    if request.method =="POST":
        form=CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.info(request,"We have sent you an verfication email")
            return redirect('login')
    
    return render(request,'accounts/signup.html')