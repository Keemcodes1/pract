from django.shortcuts import render,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse,JsonResponse 
from .models import Products
from .forms import ProductModelForm
# Create your views here.

# def home_view(request):
#     context = {'title':'Okello', 'age':36}

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
@login_required
def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    if query:
        qs = Products.objects.filter(title__icontains=query)  # Use the entire query string
    else:
        qs = Products.objects.none()

    print(query, qs)  # Ensure this is indented correctly
    context = {'title': 'okello', 'age': 36, 'query': query, 'results': qs}
    return render(request, 'home.html', context)
@staff_member_required
def product_create_view(request,*args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        form = ProductModelForm()
    # print(request.POST)
    # print(request.GET)
    # if request.method == 'POST':
    #     post_data = request.POST or None
    #     if post_data != None:
    #         my_form = ProductForm(request.POST)
    #         if my_form.is_valid():
    #             print(my_form.cleaned_data.get('title'))
    #             title_from_input = my_form.cleaned_data.get('title')
    #             Products.object.create(title=title_from_input)
            
    #         #print('post_data',post_data)



    return render(request, 'forms.html',{'form':form})

 
@login_required
def product_detail_view(request,pk):
    try:
        obj = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        raise Http404
    # 
    return render(request, 'products/details.html', {'object':obj})

@login_required
def product_api_detail_view(request,pk,*args,**kwargs):
    try:
        obj = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return JsonResponse({'message':'Not found'})
    
    return JsonResponse({'id':obj.pk})
@login_required
def product_list_view(request):
    qs = Products.objects.all()
    context = {'object_list':qs}
    return render(request, 'products/list.html', context)
