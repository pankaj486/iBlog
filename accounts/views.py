from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from blog.models import Post

from django.core.mail import send_mail
from django.conf import settings



def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # messages.success(request, 'Registration Successfull')
            # messages.success(request, 'Thank you for registring with us. We have sent you verification email to your email address. Please verify it!')
            send_mail(
                subject = 'Welcome to iBlog',
                message = request.POST['username'] + '' + 'We are glad you are here!',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [request.POST['email']],
                fail_silently=False,
            )
            return redirect('login')
        else:
            raise ValueError('username and password wrong or already exists')

    else:
        form = CustomUserCreationForm()

    context = {
    'form':form,
    }

    return render(request, 'accounts/registration.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request,'User is logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid logging credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are successfully logged out.')
    return redirect('login')


def profile(request):
    user = request.user
    profile = Profile.objects.all()
    posts = Post.objects.filter(user=user)

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        try:
            if profile_form.is_valid():
                profile_form.save()
        except Exception as e:
            return e
    else:
        profile_form = ProfileForm()

    context = {
        'profile_form': profile_form,
    }

    return render(request, 'create_profile.html', context)
