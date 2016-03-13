from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Category
from django.template import loader

def index(request):
    latest_item_list = Item.objects.order_by('-pub_date')[:12]
    context = {'latest_item_list': latest_item_list}
    return render(request, 'shop/index2.html', context)

def item_detail(request, item_id):
	return HttpResponse("You're looking at item %s." % item_id)


