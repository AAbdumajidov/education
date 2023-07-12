from django.contrib import admin
from .models import LessonFiles, Lesson, Course, SoldCourse


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'discount_price', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_date'
    autocomplete_fields = ('author', )
    search_fields = ('author__user__first_name', 'author__user_username')


class LessonFilesInline(admin.TabularInline):
    model = LessonFiles
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = (LessonFilesInline,)
    list_display = ('id', 'course', 'title', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    date_hierarchy = 'created_date'


@admin.register(SoldCourse)
class SoldCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'course', 'created_date')
    readonly_fields = ('created_date',)
    date_hierarchy = 'created_date'
    list_filter = ('course', )
    autocomplete_fields = ('profile', )

