from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ItemForm, CategoryForm
from .models import Item, Category

# Create your views here.

@login_required
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read_items')
    else:
        form = ItemForm()
    return render(request, 'core/create_item.html', {'form':form})
        

@login_required
def read_items(request):
    items = Item.objects.all()
    return render(request, 'core/read_items.html', {'items': items})

@login_required
def update_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('read_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'core/update_item.html', {'form': form})

@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('read_items')

@login_required
def item(request, id):
    item = Item.objects.get(id=id)
    user = request.user
    return render(request, 'core/item.html', {'item':item, 'user':user})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_items')
    else:
        form = CategoryForm()
    return render(request, 'core/create_category.html', {'form': form})



