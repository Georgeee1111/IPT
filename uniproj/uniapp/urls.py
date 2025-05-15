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
] 