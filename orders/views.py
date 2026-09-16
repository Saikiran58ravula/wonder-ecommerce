from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    if not cart or not cart.items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('products:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                total_amount=cart.get_total(),
            )

            for item in cart.items.all():
                if item.quantity > item.product.stock:
                    messages.error(
                        request,
                        f"Not enough stock for {item.product.name}. Only {item.product.stock} left."
                    )
                    order.delete()
                    return redirect('cart:view_cart')

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    price=item.product.price,
                    quantity=item.quantity,
                )
                item.product.stock -= item.quantity
                item.product.save()

            cart.items.all().delete()
            messages.success(request, f"Order #{order.id} placed successfully!")
            return redirect('orders:order_success', order_id=order.id)
    else:
        form = CheckoutForm()

    context = {'form': form, 'cart': cart}
    return render(request, 'orders/checkout.html', context)


@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
