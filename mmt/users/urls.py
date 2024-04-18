from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    # path('signup/', UserRegistration.as_view(), name='signup'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('test/', ProtectedAPIView.as_view(), name='test')
]