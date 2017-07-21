from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^form/$', views.PostCommentView.as_view()),
    url(r'^(?P<url_slug>[\w-]+)/$', views.BlogPostView.as_view(), name='blog_post'),

]