from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum

from .models import Stock, Gold
from .forms import StockAddForm

from pandas import Series, DataFrame
import pandas as pd
from nsetools import Nse

# Create your views here.


def home_view(request):
    # print(args,kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"base.html",{})




def stock_create_view(request):
    form = StockAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StockAddForm()

    stocks_dictionary = Nse().get_stock_codes()
    stock_names_list = list(Nse().get_stock_codes().values())
    
    
    context = {
        'form' : form,
        'stock_names_list' : stock_names_list,
        'stocks_dictionary' : stocks_dictionary
    }

    return render(request,"stocks/stock_create.html",context)


def portfolio_view(request):
    # stockset = Stock.objects.all()
    gold = Gold.objects.all()
    # value1 = Stock.objects.all().aggregate(new=(Sum('buy_price')))
    # value2 = Stock.objects.all().aggregate(new=(Sum('qty_price_mul()')))
    # new_value = Stock
    # list_of = new_value.qty_price_mul(stockset)
    # print(list_of)
    total = 0
    for i in Stock.objects.all():
        total += (i.buy_price*i.quantity)
            
    context = {
        "gold_list":gold,
        "equity_sum":total,
    }
    return render(request,"stocks/portfolio.html",context)


def stock_list_view(request):
    stockset = Stock.objects.all()

    name = []
    qty = []
    bp = []
    ttl = []
    for i in Stock.objects.all():
        name.append(i.name)
        qty.append(i.quantity)
        bp.append(i.buy_price)
        ttl.append(i.buy_price*i.quantity)

    data = {
        'name':name,
        'qty':qty,
        'bp':bp,
        'ttl':ttl
    }
    df = pd.DataFrame(data=data)

    sum_of_qty = df.groupby('name')['qty'].sum()
    sum_bp = df.groupby('name')['ttl'].sum()

    avg_bp = sum_bp/sum_of_qty

    set_name = set(name)

    new_dict = {}

    for i in set_name:
        new_dict[i] = sum_of_qty[i],avg_bp[i]

    fname = []
    fqty = []
    fbp = []
    fttl = []
    for i in set_name:
        fname.append(i)
        fqty.append(sum_of_qty[i])
        fbp.append(avg_bp[i])
        fttl.append(sum_of_qty[i]*avg_bp[i])

    urls = {}
    for i in stockset:
        urls[i.name] = i.get_absolute_url
  

    for i in range(0,len(set_name)):
        if fname[i] in urls.keys():
            print(urls[fname[i]])


    context = {
        "object_list":stockset,
        'new_dict':new_dict,
        'range':range(0,len(set_name)),
        'fname':fname,
        'fqty':fqty,
        'fbp':fbp,
        'fttl':fttl,
        'urls':urls
    }
    return render(request,"stocks/stock_list.html",context)


# def dynamic_lookup_view(request, my_id):
#     # obj = Product.objects.get(id=my_id)
#     obj = get_object_or_404(Stock, id=my_id)
#     # try:
#     #     obj = Product.objects.get(id=my_id)
#     # except Product.DoesNotExist:
#     #     raise Http404
#     context = {
#         "object":obj
#     }
#     return render(request,"stocks/stock_detail.html",context)



def single_stock_details(request, my_name):

    # stocks = get_object_or_404(Stock, name=my_name)
    single_stock = Stock.objects.filter(slug=my_name)
    first_stock_name = single_stock[0]
    print(single_stock[0].name)

    context = {
        # "object":stocks,
        "single_stock":single_stock,
        "first_stock_name":first_stock_name
    }
    return render(request,"stocks/stock_detail.html",context)


def dummy_func(request):
    stockset = Stock.objects.all()
    for i in stockset:
        if stockset.count(i.name)>1:
            print(i)
        else:
            print("Double")

    return render(request,"stocks/stock_list.html",{})






























































































# def stock_detail_view(request):
#     obj = Stock.objects.get(id=1)
#     # context = {
#     #     'title' : obj.title,
#     #     'description' : obj.description
#     # }
#     context = {
#         'object' : obj,
#         # 'value'  : obj.buy_price*obj.quantity
#     }
#     return render(request,"stocks/stock_detail.html",context)



# def with_pandas():
#     new_query = Stock.objects.all()
#     new_list = []
#     for i in new_query:
#         new_list.append(i.name)
#     data = {
#         'name': new_list
#     }
#     return render(request,"stocks/stock_detail.html",context)


# def render_initial_data(request):
#     initial_data = {
#         'title':"This is awesome"
#     }
#     obj = Stock.objects.get(id=10)
#     form = StockAddForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form':form
#     }
#     return render(request,"stocks/stock_create.html",context)




# def list_view_with_avg_bp(request):
#     name = []
#     qty = []
#     bp = []
#     ttl = []
#     for i in Stock.objects.all():
#         name.append(i.name)
#         qty.append(i.quantity)
#         bp.append(i.buy_price)
#         ttl.append(i.buy_price*i.quantity)
#     data = {
#         'name':name,
#         'qty':qty,
#         'bp':bp,
#         'ttl':ttl
#     }
#     df = pd.DataFrame(data=data)
#     sum_of_qty = df.groupby('name')['qty'].sum()
#     sum_bp = df.groupby('name')['ttl'].sum()
#     avg_bp = sum_bp/sum_of_qty
#     set_name = set(name)
#     new_dict = {}
#     for i in set_name:
#         new_dict[i] = avg_bp[i]
#     # print(new_dict)
#     # print(df)
#     # print(set_name)
#     # print(avg_bp)
#     context = {
#         "set_name":set_name,
#         "avg_bp":avg_bp,
#         'range':range(0,len(set_name)),
#         'new_dict':new_dict
#     }
#     return render(request,"stocks/portfolio.html",context)