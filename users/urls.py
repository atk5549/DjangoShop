from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (EmailVerificationView, LoginUserView,
                         UserProfileUpdateView, UserRegistrationCreateView)

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('registration/', UserRegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileUpdateView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification')
]
