from django.contrib import admin
from django.utils.html import format_html

from .models import StudioBooking, BeatPurchase


@admin.register(StudioBooking)
class StudioBookingAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'phone',
        'email',
        'service',
        'preferred_date',
        'preferred_time',
        'status',
        'payment_proof_link',
        'created_at',
    )

    list_filter = (
        'status',
        'service',
        'preferred_date',
        'created_at',
    )

    search_fields = (
        'full_name',
        'phone',
        'email',
        'project_title',
    )

    list_editable = (
        'status',
    )

    readonly_fields = (
        'created_at',
        'payment_proof_link',
    )

    ordering = (
        '-created_at',
    )

    def payment_proof_link(self, obj):
        if obj.proof_of_payment:
            return format_html(
                '<a href="{}" target="_blank">View Proof</a>',
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    payment_proof_link.short_description = "Payment Proof"


@admin.register(BeatPurchase)
class BeatPurchaseAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'phone',
        'email',
        'beat',
        'status',
        'payment_proof_link',
        'created_at',
    )

    list_filter = (
        'status',
        'beat',
        'created_at',
    )

    search_fields = (
        'full_name',
        'phone',
        'email',
    )

    list_editable = (
        'status',
    )

    readonly_fields = (
        'created_at',
        'payment_proof_link',
    )

    ordering = (
        '-created_at',
    )

    def payment_proof_link(self, obj):
        if obj.proof_of_payment:
            return format_html(
                '<a href="{}" target="_blank">View Proof</a>',
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    payment_proof_link.short_description = "Payment Proof"