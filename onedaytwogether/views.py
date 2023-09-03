from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView 
from django.views import generic
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
import datetime
class HomeView(View):
    template_name = 'index.html'
    
    def get(self, request):
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name, {'userdata': userdata})
class DestinationView(View):
    template_name = 'Destination.html'

    def get(self, request):
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        search_query = request.GET.get('search')
        data = Destination.objects.all()

        if search_query:
            data = data.filter(
                Q(destination__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return render(request, self.template_name, {'data': data,'userdata':userdata})
class ShopView(View):
    template_name = 'shop.html'
    
    def get(self, request):
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata})
class ContactView(View):
    template_name = 'contact.html'
    
    def get(self, request):
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata})
class AboutusView(View):
    template_name = 'aboutus.html'
    
    def get(self, request):
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata})
class LoginView(View):
    template_name = 'login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs): 
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onedaytwogether:index')
        else:
            return redirect('onedaytwogether:Login')
class SignupView(View):
    template_name = 'signup.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request, **kwargs):
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Create user and save
        user = User.objects.create_user(username=username, password=password,email=email)
        
        # Log in the user
        user = authenticate(request, username=username, password=password)
        login(request, user)
        
        return redirect('onedaytwogether:index')


class CompleteProfile(View):
    template_name = 'CompleteProfiles.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request, **kwargs):
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        avatar = request.FILES.get('file')
        sex = request.POST.get('sex')
        dob = request.POST.get('birthdate')
        tel = request.POST.get('phone')
        detail = request.POST.get('detail')
        address = request.POST.get('address')
        
        user_profile, created = User_Profile.objects.get_or_create(Users=user)
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.avatar = avatar
        user_profile.sex = sex
        user_profile.dob = dob
        user_profile.email = request.user.email
        user_profile.tel = tel
        user_profile.detail = detail
        user_profile.Address = address
        user_profile.status = True  # Assuming status is a BooleanField
        user_profile.save()

        return redirect('onedaytwogether:index')
class LogoutView(View):
    def get(self, request): 
        logout(request)
        return redirect('onedaytwogether:Login')
