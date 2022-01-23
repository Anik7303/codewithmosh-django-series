
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# from django.db.models.aggregates import Avg, Count, Min, Max, Sum
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField, Avg, Count, Min, Max, Sum
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Concat
from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem

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
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min(
    #     'unit_price'), max_price=Max('unit_price'), total_price=Sum('unit_price'), avg_price=Avg('unit_price'))

    # queryset = Customer.objects.annotate(is_new=True) # this line produces an error, value provided to annotate method have to be an expression (use Value, F, Func, Aggregate Classes eg. Sum, Count, Avg etc..)
    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(new_id=F('id'))
    # queryset = Customer.objects.annotate(new_id=F('id')+1)

    # Database 'CONCAT' function
    # queryset = Customer.objects.annotate(fullname=Func(
    #     F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name'))

    # queryset = Customer.objects.annotate(orders_count=Count('order'))
    # queryset = Customer.objects.annotate(orders_count=Count('order'), full_name=Func(
    #     F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price=discounted_price)

    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )

    # queryset = TaggedItem.objects.get_tags_for(Product, 5)

    # One way to create a new entry
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # # collection.featured_product_id = 1 # canbe used instead of the previous line
    # collection.save()

    # Another way to create a new entry
    # collection = Collection.objects.create(
    #     title="Video Games 2", featured_product_id=3)

    # Updating objects but there's a problem if not all fields are updated
    # collection = Collection(pk=12)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # A better way to update is this one
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    # Or another way to update
    collection = Collection.objects \
        .filter(pk=12) \
        .update(
            featured_product=Product(pk=3)
        )

    # product = []

    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'anik'})
    # return render(request, "hello.html", {"name": "anik", "product": product})
    # return render(request, "hello.html", {"name": "anik", "products": products})
    # return render(request, "hello.html", {"name": "anik", "orders": orders_qs})
    # return render(request, "hello.html", {"name": "anik", 'result': result})
    # return render(request, "hello.html", {"name": "anik", 'result': list(queryset)})
    # return render(
    #     request,
    #     "hello.html",
    #     {"name": "anik", "products": products, "result_count": products.count()},
    # )
