from django.shortcuts import render, redirect

from .forms import ContactForm
from ..models import Category
from apps.course.models import Course
from apps.account.models import Profile
from ...blog.models import Post


def index(request):
    categories = Category.objects.all()
    randomly_5_courses = Course.objects.order_by('?')[:5]
    teachers = Profile.objects.filter(role='1').order_by('?')[:3]
    last_post = Post.objects.last()
    recent_posts = Post.objects.exclude(id=last_post.id).order_by("-id")[:4]
    ctx = {
        'categories': categories,
        'randomly_5_courses': randomly_5_courses,
        'teachers': teachers,
        'last_post': last_post,
        'recent_posts': recent_posts
    }
    return render(request, 'main/index.html', ctx)


def about_view(request):

    ctx = {

    }
    return render(request, 'main/about.html', ctx)


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'main/contact.html', ctx)