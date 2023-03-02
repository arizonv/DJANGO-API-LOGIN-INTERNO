from django.urls import path , include
from django.conf import settings
from login import views

from .views import LoginFormView,LogoutView


urlpatterns = [
    path('home', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
  