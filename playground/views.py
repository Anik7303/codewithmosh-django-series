from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product

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
    product = Product.objects.latest("unit_price", "-title")

    # return HttpResponse('Hello World')
    # return render(request, 'hello.html', {'name': 'anik'})
    return render(request, "hello.html", {"name": "anik", "product": product})
    # return render(request, "hello.html", {"name": "anik", "products": products})
    # return render(
    #     request,
    #     "hello.html",
    #     {"name": "anik", "products": products, "result_count": products.count()},
    # )
