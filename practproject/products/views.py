from django.shortcuts import render,Http404
from django.http import HttpResponse,JsonResponse 
from .models import Products
# Create your views here.

# def home_view(request):
#     context = {'name':'Okello', 'age':36}

#     return render(request, 'home.html', context)
# def product_detail_view(request,pk):
#     try:
#         obj = Products.objects.get(pk=pk)
#     except Products.DoesNotExist:
#         raise Http404
   
#     return render(request, 'products/details.html', {'object':obj})

# def product_list_view(request):
#     qs = Products.objects.all()
#     context = {'object_list':qs}
#     return render(request, 'products/list.html', context)

def home_view(request,*args,**kwargs):
    # return HttpResponse('<h1>Hello world</h1>')
    context = {'name':'okello','age': 36}
    return render(request, 'home.html',context)

def product_detail_view(request,pk):
    try:
        obj = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        raise Http404
    # 
    return render(request, 'products/details.html', {'object':obj})


def product_api_detail_view(request,pk,*args,**kwargs):
    try:
        obj = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return JsonResponse({'message':'Not found'})
    
    return JsonResponse({'id':obj.pk})

def product_list_view(request):
    qs = Products.objects.all()
    context = {'object_list':qs}
    return render(request, 'products/list.html', context)
