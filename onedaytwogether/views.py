from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView 
from django.views import generic
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(View):
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, self.template_name)
class DestinationView(View):
    template_name = 'Destination.html'
    
    def get(self, request):
        return render(request, self.template_name)
class ShopView(View):
    template_name = 'shop.html'
    
    def get(self, request):
        return render(request, self.template_name)
class ContactView(View):
    template_name = 'contact.html'
    
    def get(self, request):
        return render(request, self.template_name)
class AboutusView(View):
    template_name = 'aboutus.html'
    
    def get(self, request):
        return render(request, self.template_name)
class LoginView(View):
    template_name = 'login.html'
    
    def get(self, request):
        return render(request, self.template_name)
class SignupView(View):
    template_name = 'signup.html'
    
    def get(self, request):
        return render(request, self.template_name)
