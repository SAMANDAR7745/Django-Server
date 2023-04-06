from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, UserProfileForm
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.conf import settings
from .models import UserProfile





class RegisterUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'Siz allaqachon tizimdasiz!')
            return redirect('index')
        else:
            form = NewUserForm()
            return render(request, 'forms/index.html', context={'form': form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Register successfully!')
            return redirect('index')
        else:
            messages.error(request, "Account creation failed")
            return redirect('registor')


class LogoutUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, 'Logout successfully!')

        else:
            messages.info(request, 'Siz hali tizimga kirmagansiz!')
        return redirect('index')


class LoginUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'Siz allaqachon tizimdasiz!')
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, "forms/login.html", {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in {username}.")
                return redirect('main')
            else:
                messages.error(request, 'Invalid information2')
                return redirect('login')
        else:
            messages.error(request, 'Invalid information1')
            return redirect('login')


class PasswordReset(View):
    def get(self, request):
        form = PasswordResetForm()
        return render(request, 'forms/password_reset.html', {'form': form})

    def post(self, request):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = get_object_or_404(User, email=email)
            if user:
                subject = "Password Reset Requested"
                email_template_name = "forms/password_reset_email.txt"
                data = {
                    "email": user.email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                message = render_to_string(email_template_name, data)
                try:
                    send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER,
                              recipient_list=[user.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                else:
                    return redirect('password_reset_done')
            else:
                messages.error(request, "For isn't valid")
                return redirect('password_reset')


class UserView(View):
    def get(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        return render(request, 'forms/profile.html', {'profile': user_profile})


class UserUpdateView(View):
    def get(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(instance=user_profile)
        return render(request, "forms/update_profile.html", context={'form': form})

    def post(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            address = form.cleaned_data.get('address')
            bio = form.cleaned_data.get('bio')
            website = form.cleaned_data.get('website')
            if image:
                user_profile.image = image
            user_profile.address = address
            user_profile.bio = bio
            user_profile.website = website
            user_profile.save()
            return redirect('profile')
        else:
            return redirect('update_profile')


class DeleteUser(View):
    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        profile.delete()
        user.delete()
        messages.success(request, 'User deleted successfull')
        return redirect('index')
