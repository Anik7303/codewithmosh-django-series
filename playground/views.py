from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Avg, Count, Min, Max, Sum
from store.models import Product, OrderItem, Order

# Create your views here.


def index(request):
    # query_set = Product.objects.all()
    # products = query_set[0:10]
    # try:
    #     product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #     pass
    # product = Product.objects.filter(pk=1).first()
    # product_exists = Product.objects.filter(pk=1).exists()
    # products = Product.objects.filter(unit_price__gt=20)[0:30]
    # products = Product.objects.filter(title__contains="coffee")[0:10]
    # products = Product.objects.filter(title__icontains="coffee")[:10]
    # products = Product.objects.filter(title__istartswith="co")[:10]
    # products = Product.objects.filter(title__iendswith="co")[:10]
    # products = Product.objects.filter(unit_price__range=(20, 30))[:10]
    # products = Product.objects.filter(collection__id__range=(1, 3))[0:10]
    # products = Product.objects.filter(last_update__year=2021)[:10]
    # products = Product.objects.filter(description__isnull=True)[:10]
    # AND query
    # products = Product.objects.filter(inventory__lt=10, unit_price__gt=20)
    # products = Product.objects.filter(inventory__lt=10).filter(unit_price__gt=20)
    # OR query | not query
    # products = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__gt=20))
    # products = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__gt=20))
    # products = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__gt=20))
    # products = Product.objects.filter(inventory=F("unit_price"))
    # products = Product.objects.filter(inventory=F("collection__id"))
    # products = Product.objects.filter(collection__id__range=(1, 3)).order_by(
    #     "collection__id"
    # )[:10]
    # products = Product.objects.filter(collection__id__range=(3, 5)).order_by(
    #     "-collection__id"
    # )
    # products = Product.objects.order_by("unit_price", "-title")
    # products = Product.objects.order_by("title", "-unit_price")[:50]
    # products = Product.objects.order_by("title", "-unit_price").reverse()
    # product = Product.objects.order_by('unit_price', '-title').first()
    # products = Product.objects.filter(collection__id=3).order_by("unit_price", "-title")
    # product = Product.objects.filter(collection__id=3).order_by("unit_price", "-title")[
    #     0
    # ]
    # product = (
    #     Product.objects.filter(collection__id=3)
    #     .order_by("unit_price", "-title")
    #     .first()
    # )  # next one is equivalent to this one
    # product = Product.objects.earliest("unit_price")
    # product = Product.objects.earliest("unit_price", "-title")
    # product = Product.objects.latest("unit_price", "-title")
    # products = Product.objects.filter(unit_price__lte=30)
    # products = Product.objects.filter(
    #     unit_price__lte=30).values('id', 'title')[:20]
    # products = Product.objects.filter(
    #     collection__title__icontains='co').values('title', 'id')
    # products = Product.objects.filter(
    #     unit_price__gt=20).values_list('id', 'title')  # returns a query set that contains tuples of product information

    # products = Product.objects.filter(id__in=OrderItem.objects.values(
    #     'product__id').distinct()).order_by('title')
    # products = Product.objects.filter(id__in=OrderItem.objects.values(
    #     'product__id').distinct()).order_by('title').values('title', 'unit_price')

    # defer - delays the execution of that portion of query to later when that specific enty in needed
    # products = Product.objects.only('title', 'unit_price').defer('description')
    # products = Product.objects.select_related('collection').all()
    # products = Product.objects.prefetch_related('promotions').all()
    # products = Product.objects.select_related(
    #     'collection').prefetch_related('promotions').all()[:20]

    # Exercise
    # orders_qs = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # Aggregate returns dictionary object not a query set
    # result will be a dictionary containing an entry name 'id__count'
    # result = Product.objects.aggregate(Count('id'))
    # result will be a dictionary containing an entry name 'count'
    # result = Product.objects.aggregate(count=Count('id'))
    # multiple aggregate queries entries
    result = Product.objects.aggregate(count=Count('id'), min_price=Min(
        'unit_price'), max_price=Max('unit_price'), total_price=Sum('unit_price'))

    # product = []

    # return HttpResponse('Hello World')
    # return render(request, 'hello.html', {'name': 'anik'})
    # return render(request, "hello.html", {"name": "anik", "product": product})
    # return render(request, "hello.html", {"name": "anik", "products": products})
    # return render(request, "hello.html", {"name": "anik", "orders": orders_qs})
    return render(request, "hello.html", {"name": "anik", 'result': result})
    # return render(
    #     request,
    #     "hello.html",
    #     {"name": "anik", "products": products, "result_count": products.count()},
    # )
