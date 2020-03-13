from django.shortcuts import render
from .models import List

# Create your views here.

def home(request):
	allItems = List.objects.all
	
	return render(request, 'home.html', {'all_items': allItems})
	
def about(request):
	return render(request, 'about.html', {})
