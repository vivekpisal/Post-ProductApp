from django.shortcuts import render
from .models import Product
# Create your views here.



def allproducts(request):
	template_name = 'products/allproducts.html'
	all_products = Product.objects.all().using('other')
	context = {'all_products':all_products}
	return render(request,template_name,context)
