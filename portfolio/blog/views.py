from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# Create your views here.
from .models import Category, Post, Comment


class IndexView(generic.ListView):
    template_name = 'homepage/base.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return Post.objects.order_by('-publish_date')


def index(request):
    latest_blog_posts = Post.objects.order_by('-publish_date')

    context = {
        'latest_blog_posts': latest_blog_posts,
        'page_title': "Blog",
    }

    return render(request, 'homepage/home.html', context)