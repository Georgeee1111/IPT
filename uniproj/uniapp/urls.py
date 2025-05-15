from django.urls import path
from . import views

app_name = 'uniapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_universities, name='search_universities'),
    path('trainer_registration/', views.trainer_registration, name='trainer_registration'),
    path('learn_as_trainer/', views.learn_as_trainer, name='learn_as_trainer'),
    
    # Admin URLs - Changed prefix from 'admin/' to 'dashboard/'
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/users/', views.admin_users, name='admin_users'),
    path('dashboard/users/<int:user_id>/toggle/', views.toggle_user_status, name='toggle_user_status'),
    path('dashboard/users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('dashboard/universities/', views.admin_universities, name='admin_universities'),
    path('dashboard/universities/add/', views.add_university, name='add_university'),
    path('dashboard/universities/<int:university_id>/', views.edit_university, name='get_university'),
    path('dashboard/universities/<int:university_id>/edit/', views.edit_university, name='edit_university'),
    path('dashboard/universities/<int:university_id>/delete/', views.delete_university, name='delete_university'),
] 