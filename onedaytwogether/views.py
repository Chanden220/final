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
    def post(self, request, **args): 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        avatar = request.FILES.get('avatar')
        sex = request.POST.get('sex')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        detail = request.POST.get('detail')
        address = request.POST.get('address')
        
        student = User_Profile(
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            sex=sex,
            dob=dob,
            email=email,
            tel=tel,
            detail=detail,
            status=status == 'on',  # Convert 'on' to True, otherwise False
        )
        student.save()
        return redirect('userprofile:studentlist')
    
class LogoutView(View):
    def get(self, request): 
        logout(request)
        return redirect('onedaytwogether:Login')
