from django.shortcuts import render
from .models import Tag, Project

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your views here.


def index(request):

    title = 'Web Portfolio | Erick Mutua'

    return render(request, 'index.html', {'title': title})


def project(requests):

    try:

        tags = Tag.objects.filter().all()

        projects = Project.objects.filter().all().order_by('-id')

        return render(requests, 'projects/project.html', {'tags': tags, 'projects': projects})

    except ObjectDoesNotExist:

        raise Http404()


def single_project(requests, project_name):

    try:

        project = Project.objects.get(name=project_name)

        tags = Tag.objects.filter(name=project_name).all()

        return render(requests, 'projects/project-info.html', {'project': project, 'tags': tags})

    except ObjectDoesNotExist:

        raise Http404()


def contact(request):

    try:

        return render(request, 'contact.html')

    except ObjectDoesNotExist:

        raise Http404()
