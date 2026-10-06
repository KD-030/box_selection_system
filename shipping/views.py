from django.shortcuts import render

from .forms import OrderRecommendationForm
from .models import Box, Order, OrderItem, Product


def index(request):
    form = OrderRecommendationForm(request.POST or None)
    product_list = Product.objects.all()
    box_list = Box.objects.all()
    recommendation = None
    order = None

    if request.method == 'POST' and form.is_valid():
        customer_name = form.cleaned_data['customer_name']
        order = Order.objects.create(customer_name=customer_name)
        for product, quantity in form.selected_products():
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        recommendation = order.recommend_box()

    return render(
        request,
        'shipping/index.html',
        {
            'form': form,
            'recommendation': recommendation,
            'order': order,
            'products': product_list,
            'boxes': box_list,
        },
    )
