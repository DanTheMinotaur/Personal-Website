from django.views import generic
from django.views.generic.edit import FormView
from .models import Category, Post, Comment
from .forms import CommentForm


class IndexView(generic.ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return Post.objects.order_by('-publish_date')


class BlogPostView(generic.DetailView):
    template_name = 'blog/blog_post.html'
    model = Post
    context_object_name = 'blog_post'
    slug_url_kwarg = 'url_slug'
    slug_field = 'url_slug'

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_id=context['blog_post'].id)
        context['form'] = CommentView
        return context


class CommentView(FormView):
    template_name = 'blog/comment_form.html'
    form_class = CommentForm
    success_url = '/'



