from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.conf import settings
from onedaytwogether import views as onedaytwogether_view
from . import views
from onedaytwogether.views import *
app_name = 'onedaytwogether'
urlpatterns = [
    # url('^home/$', staff_view.home_page, name='home'),
    re_path('^Home/$', onedaytwogether_view.HomeView.as_view(), name='index'),
    re_path('^Destination/$', onedaytwogether_view.DestinationView.as_view(), name='Destination'),
    re_path('^Shop/$', onedaytwogether_view.ShopView.as_view(), name='shop'),
    re_path('^Contact/$', onedaytwogether_view.ContactView.as_view(), name='contact'),
    re_path('^Aboutus/$', onedaytwogether_view.AboutusView.as_view(), name='Aboutus'),
    re_path('^Login/$', onedaytwogether_view.LoginView.as_view(), name='Login'),
    re_path('^Signup/$', onedaytwogether_view.SignupView.as_view(), name='Signup'),
    re_path('^Logout/$', onedaytwogether_view.LogoutView.as_view(), name='Logout'),
    re_path('^CompleteProfile/$', onedaytwogether_view.CompleteProfile.as_view(), name='CompleteProfile')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)