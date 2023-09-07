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
from django.contrib import messages
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
        searchdate_query = request.GET.get('searchdate')
        desdata = Destination.objects.all()
        shcedata = Schedule.objects.all().order_by('Schedule')
        
        if search_query:
            desdata = desdata.filter(
                Q(destination__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        if searchdate_query:
            schesearch = shcedata.filter(
                Q(Schedule__icontains=searchdate_query) 
            )
            desdata = desdata.filter(
                Q(schedule__in=schesearch.values('pk')) 
            )
        
        return render(request, self.template_name, {'desdata': desdata, 'shcedata': shcedata, 'userdata': userdata})
class ShopView(View):
    template_name = 'shop.html'
    
    def get(self, request):
        products = Shop.objects.filter(Quantity__gt=0)
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata,'productdata':products})
    def post(self, request, **kwargs):
        search_query = request.POST.get('search')
        product=Shop.objects.filter(Quantity__gt=0)
        if search_query:
            product = product.filter(
                Q(Product_name__icontains=search_query) |
                Q(Product_Type__icontains=search_query) |
                Q(detail__icontains=search_query)
            )
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata,'productdata':product})
class ShopCategoryView(View):
    template_name = 'shop.html'
    
    def get(self, request,category):
        products = Shop.objects.filter(Product_Type=category, Quantity__gt=0)
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata,'productdata':products})
class CartView(View):
    template_name = 'cart.html'
    
    def get(self, request):
       
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata})
class ShopDetailView(View):
    template_name = 'product-detail.html'
    
    def get(self, request,id):
        product=Shop.objects.get(id=id)
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        return render(request, self.template_name,{'userdata': userdata,'productdata':product})
class ContactView(View):
    template_name = 'contact.html'
    
    def get(self, request):
        selectdesdata=Destination.objects.filter(id=1)
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        desdata = Destination.objects.all()
        shcedata=Schedule.objects.all().order_by('Schedule')
        return render(request, self.template_name,{'desid':selectdesdata,'shcedata':shcedata,'desdata':desdata,'userdata': userdata})
    def post(self, request, **kwargs):
        schedule = request.POST.get('schedule')
        desid = request.POST.get('desid')
        selectdesdata=Destination.objects.filter(id=desid)
        selectschedata=Schedule.objects.filter(id=schedule)
        current_user = request.user.id
        userdata = User_Profile.objects.filter(Users=current_user)
        desdata = Destination.objects.all()
        shcedata=Schedule.objects.all().order_by('Schedule')
        
        Name = request.POST.get('Name')
        address = request.POST.get('address')
        Contactnum = request.POST.get('ContactNumber')
        email = request.POST.get('email')
        location_id = request.POST.get('Location')
        schedule_id = request.POST.get('Scheduleid')
        detail = request.POST.get('lettalk')

        location = Destination.objects.get(id=location_id)
        schedule = Schedule.objects.get(id=schedule_id)

        contact = Contact(
            Name=Name,
            Address=address,
            Phone_Number=Contactnum,
            Email=email,
            Destination=location,
            Schedule=schedule,
            Details=detail,
        )
        contact.save()
        
        return render(request, self.template_name,{'desid':selectdesdata,'schedule':selectschedata,'shcedata':shcedata,'desdata':desdata,'userdata': userdata})
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
        if '@' in username:
            mydata = User.objects.filter(email=username).first()
            user = authenticate(request, username=mydata.username, password=password)
        else:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onedaytwogether:index')
        else:
            error_message = 'Wrong Username or Email or Password'
            messages.error(request, error_message)
            return redirect('onedaytwogether:Login')


class SignupView(View):
    template_name = 'signup.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request, **kwargs):
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            # Email already exists
            error_message = 'Email is already registered. Please use a different email.'
            messages.error(request, error_message)
            return redirect('onedaytwogether:Signup')  # Redirect to the signup page with an error message
        if User.objects.filter(username=username).exists():
            # Email already exists
            error_message = 'Username is already taken. Please use a different one.'
            messages.error(request, error_message)
            return redirect('onedaytwogether:Signup') 
        
        # Create user and save
        user = User.objects.create_user(username=username, password=password, email=email)
        
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
