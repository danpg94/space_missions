from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('missions/', views.missions, name="missions"),
    path('contacto/', views.contacto, name="contacto"),
    path('logout/', views.signout, name="logout"),
    path('login/', views.signin, name="login"),
    path('missions/create/', views.createSpaceMission, name="createSpaceMission"),
]