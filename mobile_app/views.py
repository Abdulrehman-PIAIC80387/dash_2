from django.shortcuts import render

# Create your views here.



def dashbaord(request):
	
	return render(request, "dashbaord.html")

def add_stock(request):
	
	return render(request, "tables.html")





