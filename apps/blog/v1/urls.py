from django.urls import path
# from .views import blog_view, blog_detail_view
from django.views.generic import TemplateView
from .views import BlogView, BlogDetailView


urlpatterns = [
    # path('', blog_view, name='blog_view'),
    # path('detail/<int:pk>/', blog_detail_view, name='blog_detail'),
    # path('', TemplateView.as_view(template_name='blog/post_list.html'), name='blog')
    path('', BlogView.as_view(), name='blog'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]