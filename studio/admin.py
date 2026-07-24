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
        'payment_proof_link',
        'created_at',
    )
    list_filter = ('service', 'preferred_date', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'project_title')
    readonly_fields = ('created_at', 'payment_proof_link')

    def payment_proof_link(self, obj):
        if obj.proof_of_payment:
            return format_html(
                '<a href="{}" target="_blank">View Proof</a>',
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    payment_proof_link.short_description = "Proof"


@admin.register(BeatPurchase)
class BeatPurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'email',
        'beat',
        'payment_proof_link',
        'created_at',
    )
    list_filter = ('beat', 'created_at')
    search_fields = ('full_name', 'phone', 'email')
    readonly_fields = ('created_at', 'payment_proof_link')

    def payment_proof_link(self, obj):
        if obj.proof_of_payment:
            return format_html(
                '<a href="{}" target="_blank">View Proof</a>',
                obj.proof_of_payment.url
            )
        return "No proof uploaded"

    payment_proof_link.short_description = "Proof"