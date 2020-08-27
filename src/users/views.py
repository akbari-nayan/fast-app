from django.shortcuts import render, redirect
from django.views.generic import RedirectView,TemplateView,FormView,View
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout
from django.contrib import auth, messages
from django.utils.http import is_safe_url
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "posts/posts_list.html"


class UserCreateView(FormView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        request=self.request
        next_=request.GET.get('next')
        next_post=request.POST.get('next')
        redirect_path=next_ or next_post or None
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                auth_login(self.request, user)
            except user.DoesNotExist:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            messages.info(self.request, f"You are now logged in as {username}")
        else:
            messages.error(request, "Invalid username or password.")
        return super().form_valid(form)



class LogoutView(RedirectView):

    url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)








        # navbar
        # <!-- <li><a href="{% url 'users:logout-view' %}">Logout </a></li> -->
        #         {% else %}
        #         <li><a href="{% url 'users:login-view' %}">Login </a></li>
        #         <li><a href="{% url 'users:register-view' %}">Register</a></li>