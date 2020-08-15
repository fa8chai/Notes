from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate
from .forms import CustomUserCreationForm
from home.views import main
from .models import CustomUser
User = CustomUser

def login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, user, password)
        if user:
            redirect(main)
        else:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return render(request, 'users/login.html', {'error':"This email address does't belong to an account"})
            return render(request, 'users/login.html', {'error':"Invalid Credentials"})
    return render(request, 'users/login.html', {})

def signup(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            redirect(main)
        else:
            return render(request, 'users/signup.html',{'form':form})
    return render(request, 'users/signup.html',{})



@login_required
def signout(request):
    logout(request)
    return redirect(login)