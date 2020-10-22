from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path("signout", views.signout, name="signout"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test'),
    path('ajaxx/', views.ajaxx, name='ajax'),

] 
