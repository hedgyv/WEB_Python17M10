from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import RegisterForm
from .users_to_mongo import save_user_to_mongodb
from .mongo_to_postgres import migrate_to_postgres


class RegisterView(View):
    template_name = 'app_users/register.html'
    form_class = RegisterForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(form.save())
            username = form.cleaned_data["username"]
            save_user_to_mongodb(form.save())
            migrate_to_postgres()
            messages.success(request, f"Вітаємо {username}. Ваш акаунт успішно створено")
            return redirect(to="app_users:signin")
        return render(request, self.template_name, {"form": form})
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app_users/password_reset.html'
    email_template_name = 'app_users/password_reset_email.html'
    html_email_template_name = 'app_users/password_reset_email.html'
    success_url = reverse_lazy('app_users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'app_users/password_reset_subject.txt'
