from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Product
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponseBadRequest
import json
from django.core import serializers
from django.shortcuts import render_to_response

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

def product_list(request, template_name='products/product_list.html'):
    query = request.POST.get('term', '')
    if query:
        #keyword = request.POST['term']
        qset = (
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(Quantity__icontains=query)
        )
        products = Product.objects.filter(qset).distinct()
        data = {}
        data['object_list'] = products
        return render(request, template_name, data)
    else:
        products = Product.objects.all()
        data = {}
        data['object_list'] = products
    return render(request, template_name, data)

def product_create(request, template_name='products/product_form.html'):
    form = ProductForm(request.POST or None)
    if request.is_ajax() or request.method == 'POST':
        if form.is_valid():
            form.save()
            data = {}
            data['something'] = Product.objects.all().last().id
            return HttpResponse(json.dumps(data), content_type = "application/json")
            #import pdb; pdb.set_trace()
    return render(request, template_name, {'form':form})

def product_update(request, pk, template_name='products/product_form.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.is_ajax() or request.method == 'POST':
        if form.is_valid():
            form.save()
            data = '<tr id="row_'+str(product.id)+'"><td><a href="/products/edit/'+str(product.id)+'"> '+product.name+' </a></td><td> '+str(product.price)+' </td> <td> '+str(product.Quantity)+'</td><td><a delete-id="'+str(product.id)+'" href="/products/delete/'+str(product.id)+'", class="delete-button" >delete</a></td></tr>'
            return HttpResponse(data, content_type = "application/html")
    return render(request, template_name, {'form':form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.is_ajax() or request.method == 'POST':
        data = {}
        data['something'] = product.name
        product.delete()
        return HttpResponse(json.dumps(data), content_type = "application/json")
    return render(request, {'object':product})




