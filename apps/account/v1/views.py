from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from ...course.models import Course, SoldCourse
from ..models import Profile


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            messages.success(request, 'You did log in!')
            return redirect('main:index')
    ctx = {
        'form': form
    }
    return render(request, 'account/login.html', ctx)


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    ctx = {
        'form': form
    }
    return render(request, 'account/register.html', ctx)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:index')
    return render(request, 'account/logout.html')


def dashboard(request):
    user = request.user.profile
    ctx = {
        'user': user
    }
    return render(request, 'account/dashboard.html', ctx)


def my_course(request):
    courses = SoldCourse.objects.filter(profile_id=request.user.profile.id)
    ctx = {
        'courses': courses
    }
    return render(request, 'account/my_course.html', ctx)


def profile_edit(request):
    user = request.user
    profile = Profile.objects.get(user_id=user)
    if request.method == "POST":
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        image = request.FILES.get('image', None)
        print(image)
        bio = request.POST.get('bio', None)

        user.first_name = first_name
        user.last_name = last_name
        if image:
            profile.image = image
        profile.bio = bio
        user.save()
        profile.save()
        return redirect('account:dashboard')


    ctx = {
        'user': user
    }
    return render(request, 'account/profile_edit.html', ctx)
