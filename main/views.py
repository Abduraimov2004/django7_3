from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from .models import User, Course, Category, Tag, Contact
from django.contrib.messages import warning, success
from .utils import send_verification_email
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView


# Create your views here.


class HomePageView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = "courses"
    paginate_by = 3


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone = request.POST.get('phone')

        if password != password_confirm:
            warning(request, 'Password confirmation is incorrect')
            return redirect(reverse('main:register'))
        if User.objects.filter(username=username).exists():
            warning(request, 'User already registered')
            return redirect(reverse('main:register'))
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password,
                                        phone=phone, is_active=False)
        send_verification_email(user)
        login(request, user)
        success(request, 'User  registered')
        return redirect(reverse("main:kirish"))


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            warning(request, 'User does not exist')
            return redirect(reverse('main:kirish'))
        user = User.objects.get(username=username)
        if not user.check_password(password):
            warning(request, 'Password is incorrect')
            return redirect(reverse('main:kirish'))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main:home'))
        warning(request, 'Error')
        return redirect(reverse('main:kirish'))


class ContactView(View):
    def get(self, request):
        return render(request, 'contact_us.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Forma ma'lumotlarini tekshirish
        if not first_name or not last_name or not email or not subject or not message:
            return render(request, 'contact_us.html', {
                'error': 'All fields are required.'
            })

        # Forma ma'lumotlarini saqlash
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message
        )

        # Success message
        return render(request, 'contact_us.html', {
            'success': 'Your message has been sent successfully.'
        })
