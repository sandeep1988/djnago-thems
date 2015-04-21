from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from products.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

def product_list(request, template_name='products/product_list.html'):
    if request.POST:
        keyword = request.POST['term']
        products = Product.objects.filter(name__contains = keyword)
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
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def product_update(request, pk, template_name='products/product_form.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def product_delete(request, pk, template_name='products/product_confirm_delete.html'):
    product = get_object_or_404(Product, pk=pk)    
    if request.method=='POST':
        product.delete()
        return redirect('/')
    return render(request, template_name, {'object':product})
