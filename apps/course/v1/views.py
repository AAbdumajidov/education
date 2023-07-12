from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..models import Course, Lesson, LessonFiles
from apps.blog.models import Category, Tag


class CourseListView(ListView):
    queryset = Course.objects.all()
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recent_courses'] = Course.objects.order_by('-id')[:3]
        ctx['categories'] = Category.objects.all()
        ctx['tags'] = Tag.objects.all()
        return ctx


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = 'course/course_detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recent_courses'] = Course.objects.order_by('-id')[:3]
        ctx['categories'] = Category.objects.all()
        ctx['tags'] = Tag.objects.all()
        ctx['randomly_5_courses'] = Course.objects.order_by('?')[:5]
        return ctx


def lesson_detail(request, course_id,  pk):
    lesson = Lesson.objects.get(id=pk)
    main_lesson = LessonFiles.objects.filter(lesson_id=pk, is_main=True).first()
    randomly_5_courses = Course.objects.order_by('?')[:5]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    recent_courses = Course.objects.order_by('-id')[:3]
    ctx = {
        'lesson': lesson,
        'main_lesson': main_lesson,
        'randomly_5_courses': randomly_5_courses,
        'tags': tags,
        'categories': categories,
        'recent_courses': recent_courses,
    }
    return render(request, 'course/course_lesson.html', ctx)
