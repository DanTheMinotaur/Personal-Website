from django.db import models
from datetime import date


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_description = models.CharField(max_length=220, blank=True)
    slug = models.SlugField(blank=False, max_length=100)

    def __str__(self):
        return self.category_name


# Model for each blog post
class Post(models.Model):
    # Text Fields
    post_title = models.CharField(max_length=120)
    sub_heading = models.CharField(max_length=220, blank=True)
    main_content = models.TextField(max_length=10000)

    # Main Content Image
    heading_image = models.ImageField(upload_to='blog/images/')

    url_slug = models.SlugField(max_length=40, blank=True)

    # Meta Info for HTML
    meta_description = models.CharField(max_length=200)
    meta_keywords = models.CharField("Separate Keywords by commas", max_length=200)

    # Date/Time Info
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateField(default=date.today)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

