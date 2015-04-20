from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from categories.models import Category

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
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, template_name, {'form':form})

def category_update(request, pk, template_name='categories/category_form.html'):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, template_name, {'form':form})

def category_delete(request, pk, template_name='categories/category_confirm_delete.html'):
    category = get_object_or_404(Category, pk=pk)    
    if request.method=='POST':
        category.delete()
        return redirect('category_list')
    return render(request, template_name, {'object':category})