from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def home(request):
	
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			allItems = List.objects.all
			messages.success(request,('the item has been added to the DataBase!'))
			return render(request, 'home.html', {'all_items': allItems})
	else:
		allItems = List.objects.all
		return render(request, 'home.html', {'all_items': allItems})
	
def about(request):
	return render(request, 'about.html', {})
	
def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('the item has been delete from the DataBase!'))
	return redirect('home')

def crossOff(request, list_id):
	item = List.objects.get(pk=list_id)
	if item.completed == True:
		item.completed = False
		item.save()
	else:
		item.completed = True
		item.save()
	return redirect('home') 