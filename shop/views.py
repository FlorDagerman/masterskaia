from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product, Order, OrderItem
from .cart import Cart

def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'total_items': cart.get_total_items()})
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart_detail')

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            delivery_address=request.POST['address'],
            comment=request.POST.get('comment', ''),
            total_price=cart.get_total_price()
        )
        for product_id, item in cart.cart.items():
            product = Product.objects.get(id=int(product_id))
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=item['price']
            )
        cart.clear()
        return render(request, 'shop/order_confirmation.html', {'order': order})
    return render(request, 'shop/checkout.html', {'cart': cart})