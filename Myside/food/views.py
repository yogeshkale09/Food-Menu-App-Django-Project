
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.shortcuts import render, redirect
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list=Item.objects.all()
    template = loader.get_template('food/index.html')
    context ={
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)


def create_item(request):
    # Instantiate the form with POST data or None for GET requests
    form = ItemForm(request.POST or None)
    
    # Validate and save the form
    if form.is_valid():
        form.save()
        # Redirect to the index page after successful form submission
        return redirect('food:index')
    
    # Render the form template with the form object in the context
    return render(request, 'food/item-form.html',{'form': form})


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})
    