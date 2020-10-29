from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path("signout", views.signout, name="signout"),
    path('ajaxx/', views.ajaxx, name='ajax'),

] 

