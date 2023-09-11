from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from apps.directory.models import Category


# Create your views here.
@login_required()
def index(request):
    # numcategories = Category.objects.all()

    context = {'PageTitle': 'Directory', 'NumRecord': Category.objects.all().count()}

    html_template = loader.get_template('directory/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required()
def load_data(request):
    # object_list = Category.objects.all()
    object_list = Category.objects.values('pk', 'name', 'sku')


    # json = serializers.serialize('json', object_list)
    # return HttpResponse(json, content_type='application/json')
    return HttpResponse(object_list)