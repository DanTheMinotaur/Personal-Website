from django.contrib import admin
from .models import HomepageLink, HomepageSkill, HomepageSkillGroup

# Register your models here.
admin.site.register([HomepageLink, HomepageSkill, HomepageSkillGroup])
