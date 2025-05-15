from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth.models import User, auth 
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'lms/home.html')

def search_universities(request):
    query = request.GET.get('query', '')
    course_level = request.GET.get('course_level', '')
    location = request.GET.get('location', '')
    field_of_study = request.GET.get('field_of_study', '')
    
    # For now, return to home page with empty results
    # TODO: Implement actual search functionality
    context = {
        'query': query,
        'course_level': course_level,
        'location': location,
        'field_of_study': field_of_study,
        'results': []
    }
    return render(request, 'lms/home.html', context)

def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('uniapp:user_registration')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('uniapp:user_registration')
        else:
            if password == confirm_password:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()
                print('User Created')
                print(f'First Name: {first_name}')
                return redirect('uniapp:login')
            else:
                print("Password not matching...")
                messages.error(request, 'Passwords do not match')
                return redirect('uniapp:user_registration')

    else:
        return render(request, 'lms/user_registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/') 
        else:
            messages.info(request, 'Invalid credentials') 
            return redirect('uniapp:login') 
    else:
        return render(request, 'lms/login.html')


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
                return redirect('uniapp:trainer_registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('uniapp:trainer_registration')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = user_name, email = email, password = password1)
                user.is_staff=True
                user.save()
                trainer_registration = TrainerRegistration.objects.create(user = user, status = False)
                return redirect('uniapp:login')
        else:
            print("password not matching...")
            return redirect('uniapp:trainer_registration')
        return redirect('/')
    else:
        return render(request, 'lms/trainer_registration.html')

def learn_as_trainer(request):
    user = request.user
    trainer_registration = TrainerRegistration.objects.create(user = user, status = False)
    user_info = User.objects.filter(username = user.username)
    for info in user_info:
        if info.username:
            user.is_staff=True
            user.save()

    return render(request, 'lms/learn_as_trainer.html')

       
