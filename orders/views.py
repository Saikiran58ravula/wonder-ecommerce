import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from cart.models import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


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
            for item in cart.items.all():
                if item.quantity > item.product.stock:
                    messages.error(
                        request,
                        f"Not enough stock for {item.product.name}. Only {item.product.stock} left."
                    )
                    return redirect('cart:view_cart')

            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                total_amount=cart.get_total(),
            )

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    product_name=item.product.name,
                    price=item.product.price,
                    quantity=item.quantity,
                )

            amount_in_paise = int(order.total_amount * 100)
            razorpay_order = client.order.create({
                'amount': amount_in_paise,
                'currency': 'INR',
                'payment_capture': 1,
            })

            order.razorpay_order_id = razorpay_order['id']
            order.save()

            context = {
                'order': order,
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'razorpay_order_id': razorpay_order['id'],
                'amount_in_paise': amount_in_paise,
            }
            return render(request, 'orders/payment.html', context)
    else:
        form = CheckoutForm()

    context = {'form': form, 'cart': cart}
    return render(request, 'orders/checkout.html', context)


@csrf_exempt
@login_required
def payment_success(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        order = get_object_or_404(Order, id=order_id, user=request.user)

        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature,
        }

        try:
            client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            messages.error(request, "Payment verification failed. Please contact support.")
            return redirect('orders:order_history')

        order.razorpay_payment_id = razorpay_payment_id
        order.razorpay_signature = razorpay_signature
        order.is_paid = True
        order.status = 'paid'
        order.save()

        for item in order.items.all():
            if item.product:
                item.product.stock -= item.quantity
                item.product.save()

        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()

        messages.success(request, f"Payment successful! Order #{order.id} confirmed.")
        return redirect('orders:order_success', order_id=order.id)

    return redirect('products:home')


@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
