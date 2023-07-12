from django.urls import path
from .views import CourseListView, CourseDetailView, lesson_detail

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('detail/<int:course_id>/lesson/<int:pk>', lesson_detail, name='course_lesson_detail')
]