from django.contrib import admin
from .models import Tag, Project

# Register your models here.


class ProjectTag(admin.ModelAdmin):

    filter_horizontal = ('tags',)


admin.site.register(Tag)
admin.site.register(Project)
