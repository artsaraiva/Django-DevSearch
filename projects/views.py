from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Projects')


def project(request, pk):
    return HttpResponse('Project' + ' ' + pk)
