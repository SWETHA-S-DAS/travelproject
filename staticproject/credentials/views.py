from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']
        password1 = request.POST['cpassword']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'user already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'mail id already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                first_name=firstname,
                                                last_name=lastname,
                                                email=email,
                                                password=password, )

                user.save();
                print('user created')
        else:
            messages.info(request, 'password not matches')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')