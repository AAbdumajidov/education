from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('v1/', include('apps.main.v1.urls'))
]