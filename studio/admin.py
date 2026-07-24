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
        'payment_proof_preview',
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
        'payment_proof_preview',
    )

    ordering = (
        '-created_at',
    )

    def payment_proof_preview(self, obj):
        if obj.proof_of_payment:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" width="120" style="border-radius:6px;border:1px solid #ccc;" />'
                '</a>',
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    payment_proof_preview.short_description = "Payment Proof"


@admin.register(BeatPurchase)
class BeatPurchaseAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'phone',
        'email',
        'beat',
        'status',
        'payment_proof_preview',
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
        'payment_proof_preview',
    )

    ordering = (
        '-created_at',
    )

    def payment_proof_preview(self, obj):
        if obj.proof_of_payment:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" width="120" style="border-radius:6px;border:1px solid #ccc;" />'
                '</a>',
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    payment_proof_preview.short_description = "Payment Proof"