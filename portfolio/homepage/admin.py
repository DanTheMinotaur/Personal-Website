from django.contrib import admin
from .models import HomepageLink, HomepageSkills, HomepageSkillGroup

# Register your models here.
admin.site.register([HomepageLink, HomepageSkills, HomepageSkillGroup])
