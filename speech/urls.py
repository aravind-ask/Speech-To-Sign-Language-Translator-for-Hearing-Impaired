
from . import views
from django.urls import path

urlpatterns = [
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('animation/',views.animation_view,name='animation'),
    path('',views.home_view,name='home'),
    path('animation/',views.animation_view,name='animation')
]
