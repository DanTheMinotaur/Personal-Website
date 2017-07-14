from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic


# Create your views here.
from .models import Category, Post, Comment


class IndexView(generic.ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return Post.objects.order_by('-publish_date')


class BlogPostView(generic.DetailView):
    template_name = 'blog/blog_post.html'
    model = Post
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        return get_object_or_404(Post)


def blog_detail(request, slug):
    blog = get_object_or_404(Post, url_slug=slug)
    return render(request, 'blog/blog_post.html', {'blog': blog})


