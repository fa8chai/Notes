from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate
from .forms import CustomUserCreationForm
from .models import CustomUser
User = CustomUser


def signin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('main')
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
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'users/signup.html',{'form':form,})
    return render(request, 'users/signup.html',{'form':form,})



@login_required
def signout(request):
    logout(request)
    return redirect(signin)