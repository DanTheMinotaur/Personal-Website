from django.contrib import admin
from .models import Project, Skill, SkillGroup

# Register your models here.
admin.site.register([Project, Skill, SkillGroup])
