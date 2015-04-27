from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from categories.models import Category
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponseBadRequest
import json
from django.core import serializers
from django.shortcuts import render_to_response

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

def category_list(request, template_name='categories/category_list.html'):
    categories = Category.objects.all()
    data = {}
    data['object_list'] = categories
    return render(request, template_name, data)

def category_create(request, template_name='categories/category_form.html'):
    form = CategoryForm(request.POST or None)
    if request.is_ajax() or request.method == 'POST':
        if form.is_valid():
            form.save()
            data = {}
            data['something'] = Category.objects.all().last().id
            return HttpResponse(json.dumps(data), content_type = "application/json")
    return render(request, template_name, {'form':form})

def category_update(request, pk, template_name='categories/category_form.html'):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if request.is_ajax() or request.method == 'POST':
        if form.is_valid():
            form.save()
            data = '<tr id="row_'+str(category.id)+'"><td><a href="/categories/edit/'+str(category.id)+'">'+category.name+'</a></td></tr>'
            return HttpResponse(json.dumps(data), content_type = "application/json")
    return render(request, template_name, {'form':form})

def category_delete(request, pk, template_name='categories/category_confirm_delete.html'):
    category = get_object_or_404(Category, pk=pk)    
    if request.method=='POST' or request.is_ajax():
        data = {}
        data['something'] = category.id
        category.delete()
        return HttpResponse(json.dumps(data), content_type = "application/json")
    return render(request, template_name, {'object':category})