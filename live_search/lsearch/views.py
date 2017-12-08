from django.shortcuts import render, HttpResponse, render_to_response
from .models import key
from django.http import HttpRequest,JsonResponse


def search(request):
    return (render(request, 'lsearch/templates.html'))


def get_search(request):
    cat_list = []
    keyword = ''
    if request.method == 'GET':
        keyword = request.GET['suggest']
    if keyword:
        cat_list = key.objects.filter(k__icontains=keyword)

    return cat_list
