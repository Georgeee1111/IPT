from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth 
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import University
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime, timedelta

def home(request):
    # Get all universities for the featured section
    featured_universities = University.objects.all()[:6]  # Limit to 6 universities
    return render(request, 'lms/home.html', {'results': featured_universities})

def search_universities(request):
    query = request.GET.get('query', '')
    course_level = request.GET.get('course_level', '')
    location = request.GET.get('location', '')
    field_of_study = request.GET.get('field_of_study', '')
    
    # Start with all universities
    universities = University.objects.all()
    
    # Apply filters based on search parameters
    if query:
        universities = universities.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    
    if course_level:
        universities = universities.filter(course_level=course_level)
    
    if location:
        universities = universities.filter(city=location)
    
    if field_of_study:
        universities = universities.filter(field_of_study=field_of_study)
    
    context = {
        'query': query,
        'course_level': course_level,
        'location': location,
        'field_of_study': field_of_study,
        'results': universities
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
            # Check if user is staff/admin and redirect accordingly
            if user.is_staff:
                return redirect('uniapp:admin_dashboard')
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

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    # Get statistics
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    total_universities = University.objects.count()
    new_users_today = User.objects.filter(
        date_joined__gte=timezone.now() - timedelta(days=1)
    ).count()

    # Get recent users and universities
    recent_users = User.objects.order_by('-date_joined')[:5]
    recent_universities = University.objects.order_by('-id')[:5]

    context = {
        'total_users': total_users,
        'active_users': active_users,
        'total_universities': total_universities,
        'new_users_today': new_users_today,
        'recent_users': recent_users,
        'recent_universities': recent_universities,
    }
    return render(request, 'lms/admin_dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def admin_users(request):
    search_query = request.GET.get('search', '')
    status = request.GET.get('status', '')

    # Filter users
    users = User.objects.all()
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    if status:
        users = users.filter(is_active=(status == 'active'))

    # Pagination
    paginator = Paginator(users.order_by('-date_joined'), 10)
    page = request.GET.get('page')
    users = paginator.get_page(page)

    context = {
        'users': users,
        'search_query': search_query,
        'status': status,
    }
    return render(request, 'lms/admin_users.html', context)

@login_required
@user_passes_test(is_admin)
def admin_universities(request):
    search_query = request.GET.get('search', '')
    city = request.GET.get('city', '')
    field = request.GET.get('field', '')

    # Filter universities
    universities = University.objects.all()
    if search_query:
        universities = universities.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if city:
        universities = universities.filter(city=city)
    if field:
        universities = universities.filter(field_of_study=field)

    # Pagination
    paginator = Paginator(universities.order_by('name'), 10)
    page = request.GET.get('page')
    universities = paginator.get_page(page)

    # Get choices for filters
    cities = University.CITY_CHOICES
    fields = University.FIELD_OF_STUDY_CHOICES
    course_levels = University.COURSE_LEVEL_CHOICES

    context = {
        'universities': universities,
        'search_query': search_query,
        'city': city,
        'field': field,
        'cities': cities,
        'fields': fields,
        'course_levels': course_levels,
    }
    return render(request, 'lms/admin_universities.html', context)

@login_required
@user_passes_test(is_admin)
def toggle_user_status(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.is_active = not user.is_active
        user.save()
    return redirect('uniapp:admin_users')

@login_required
@user_passes_test(is_admin)
def delete_user(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.delete()
    return redirect('uniapp:admin_users')

@login_required
@user_passes_test(is_admin)
def add_university(request):
    if request.method == 'POST':
        University.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            city=request.POST['city'],
            field_of_study=request.POST['field_of_study'],
            course_level=request.POST['course_level'],
            image_url=request.POST['image_url']
        )
    return redirect('uniapp:admin_universities')

@login_required
@user_passes_test(is_admin)
def edit_university(request, university_id):
    university = University.objects.get(id=university_id)
    if request.method == 'POST':
        university.name = request.POST['name']
        university.description = request.POST['description']
        university.city = request.POST['city']
        university.field_of_study = request.POST['field_of_study']
        university.course_level = request.POST['course_level']
        university.image_url = request.POST['image_url']
        university.save()
        return redirect('uniapp:admin_universities')
    
    # Return university data for AJAX request
    return JsonResponse({
        'name': university.name,
        'description': university.description,
        'city': university.city,
        'field_of_study': university.field_of_study,
        'course_level': university.course_level,
        'image_url': university.image_url
    })

@login_required
@user_passes_test(is_admin)
def delete_university(request, university_id):
    if request.method == 'POST':
        university = University.objects.get(id=university_id)
        university.delete()
    return redirect('uniapp:admin_universities')

       
