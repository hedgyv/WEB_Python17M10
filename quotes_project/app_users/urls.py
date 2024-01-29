from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = "app_users"

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/',
         LoginView.as_view(template_name='app_users/login.html', form_class=LoginForm), name='signin'),
    path('logout/', LogoutView.as_view(template_name='app_users/logout.html'), name='logout'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='app_users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='app_users/password_reset_confirm.html',
                                          success_url='/users/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='app_users/password_reset_complete.html'),
         name='password_reset_complete'),
]   