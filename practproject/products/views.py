from django.shortcuts import render,Http404
from django.http import HttpResponse,JsonResponse 
from .models import Products
from .forms import ProductForm
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

from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    if query:
        qs = Products.objects.filter(name__icontains=query)  # Use the entire query string
    else:
        qs = Products.objects.none()

    print(query, qs)  # Ensure this is indented correctly
    context = {'name': 'okello', 'age': 36, 'query': query, 'results': qs}
    return render(request, 'home.html', context)

def product_create_view(request,*args, **kwargs):
    
    print(request.POST)
    print(request.GET)
    if request.method == 'POST':
        post_data = request.POST or None
        if post_data != None:
            my_form = ProductForm(request.POST)
            if my_form.is_valid():
                print(my_form.cleaned_data.get('name'))
                name_from_input = my_form.cleaned_data.get('name')
                Products.object.create(name=name_from_input)
            
            #print('post_data',post_data)



    return render(request, 'forms.html',{})

 

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
