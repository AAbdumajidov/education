from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from apps.blog.models import Post, Comment
from apps.blog.models import Category, Tag
from apps.course.models import Course

# def blog_view(request):
#     ctx = {
#
#     }
#     return render(request, 'blog/blog.html', ctx)
#
#
# def blog_detail_view(request, pk):
#     ctx = {
#
#     }
#     return render(request, 'blog/blog-single.html', ctx)


class BlogView(generic.ListView):
    # template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data()
        ctx['categories'] = Category.objects.all()
        ctx['tags'] = Tag.objects.all()
        ctx['recent_courses'] = Course.objects.order_by('-id')[:3]
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        if cat:
            qs = qs.filter(category__title__exact='cat')
        if tag:
            qs = qs.filter(tags__title__exact='tag')
        return qs


class BlogDetailView(generic.View):
    template_name = 'blog/blog-single.html'
    queryset = Post.objects.all()

    def get_object(self, pk, *args, **kwargs):
        try:
            post = self.queryset.get(id=pk)
        except Post.DoesNotExist:
            raise Http404
        return post

    def get_context_data(self, pk, *args, **kwargs):
        ctx = {
            'object':self.get_object(pk)
        }
        return ctx

    def get(self, request, pk):
        ctx = self.get_context_data(pk)
        comments = Comment.objects.filter(post_id=pk, parent_comment__isnull=True)
        ctx['comments'] = comments
        return render(request, self.template_name, ctx)

    def post(self, request, pk, *args, **kwargs):
        ctx = self.get_context_data(pk)
        if not request.user.is_authenticated:
            return redirect('account:login')

        comment_id = request.GET.get('comment_id', None)
        user_id = request.user.id
        body = request.POST.get('body')
        if body:
            obj = Comment.objects.create(author_id=user_id, post_id=pk, body=body, parent_comment_id=comment_id)
            return redirect(reverse_lazy('blog:blog_detail#comments', kwargs={"pk": pk}))
        return render(request, self.template_name, ctx)

