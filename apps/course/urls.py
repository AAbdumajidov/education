from django.urls import path, include

app_name = 'course'

urlpatterns = [
    path('v1/', include('apps.course.v1.urls'))
]