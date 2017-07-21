from django import forms
from django.contrib import admin
from .models import Post, Category, Comment
from ckeditor.widgets import CKEditorWidget

# Class to overwrite the default Admin Form and Add CKEditor to main_content form
class PostAdminForm(forms.ModelForm):
    main_content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ('',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'date_created')
    prepopulated_fields = {'url_slug': ('post_title',)}

    form = PostAdminForm


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register([Category, Comment])