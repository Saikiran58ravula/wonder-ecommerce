from django.contrib import admin
from django.utils import timezone
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'status', 'is_paid', 'total_amount', 'created_at')
    list_filter = ('status', 'is_paid', 'created_at')
    search_fields = ('full_name', 'user__username', 'tracking_number')
    inlines = [OrderItemInline]
    actions = ['mark_as_shipped', 'mark_as_delivered', 'cancel_orders']
    fields = (
        'user', 'full_name', 'address', 'phone', 'status', 'is_paid', 'total_amount',
        'tracking_number', 'shipped_at', 'delivered_at',
        'razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature', 'created_at',
    )
    readonly_fields = ('created_at', 'razorpay_order_id', 'razorpay_payment_id', 'razorpay_signature')

    @admin.action(description='Mark selected orders as Shipped')
    def mark_as_shipped(self, request, queryset):
        queryset.update(status='shipped', shipped_at=timezone.now())

    @admin.action(description='Mark selected orders as Delivered')
    def mark_as_delivered(self, request, queryset):
        queryset.update(status='delivered', delivered_at=timezone.now())

    @admin.action(description='Cancel selected orders')
    def cancel_orders(self, request, queryset):
        queryset.update(status='cancelled')
