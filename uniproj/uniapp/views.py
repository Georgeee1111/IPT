from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth 

def home(request):
    return render(request, 'uniapp/home.html')

def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=user_name).exists():
            messages.info(request, 'Username Taken')
            return redirect('user_registration')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('user_registration')
        else:
            if password1 == password2:
                user = User.objects.create_user(
                    username=user_name,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password1
                )
                user.save()
                print('User Created')
                print(f'First Name: {first_name}')
                return redirect('login')
            else:
                print("Password not matching...")
                messages.error(request, 'Passwords do not match')
                return redirect('user_registration')

    else:
        return render(request, 'uniapp/user_registration.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/') 
        else:
            messages.info(request, 'Invalid credentials') 
            return redirect('login') 
    else:
        return render(request, 'uniapp/login.html')


def logout(request):
    auth.logout(request) 
    return redirect('/')

def trainer_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('trainer_registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('trainer_registration')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = user_name, email = email, password = password1)
                user.is_staff=True
                user.save()
                trainer_registration = TrainerRegistration.objects.create(user = user, status = False)
                return redirect('login')
        else:
            print("password not matching...")
            return redirect('trainer_registration')
        return redirect ('/')
    else:
        return render(request, 'uniapp/trainer_registration.html')

def learn_as_trainer(request):
    user = request.user
    trainer_registration = TrainerRegistration.objects.create(user = user, status = False)
    user_info = User.objects.filter(username = user.username)
    for info in user_info:
        if info.username:
            user.is_staff=True
            user.save()

    return render(request, 'uniapp/learn_as_trainer.html')

       
