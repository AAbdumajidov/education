from django.db import models
from apps.main.models import Category, Tag
from ckeditor.fields import RichTextField
from apps.account.models import Profile


class Timestamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def file_path_for_cover(instance, filename):
    return f"courses/{instance.id}/cover/{filename}"


class Course(Timestamp):
    DIFFICULTY = (
        (0, 'beginner'),
        (1, 'intermediate'),
        (2, 'Advanced'),
    )
    title = models.CharField(max_length=221)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, limit_choices_to={"role": 1})
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    cover = models.ImageField(upload_to=file_path_for_cover, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    body = RichTextField()
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    discount_price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


def file_path(instance, filename):
    return f"courses/{instance.lesson.course.title}/{instance.lesson.title}/{filename}"


class Lesson(Timestamp):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    body = RichTextField()

    def __str__(self):
        return self.title


class LessonFiles(Timestamp):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_path)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson.title


class SoldCourse(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={"role":0})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} -> {self.course.title}"
