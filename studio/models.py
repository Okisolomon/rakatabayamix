from django.db import models

class StudioBooking(models.Model):
    SERVICE_CHOICES = [
        ('Recording', 'Recording - 100K'),
        ('Mixing', 'Mixing - 200K'),
        ('Mastering', 'Mastering - 100K'),
        ('Full Production', 'Full Production - 400K'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    project_title = models.CharField(max_length=150, blank=True)
    message = models.TextField(blank=True)
    proof_of_payment = models.ImageField(upload_to='payment_proofs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"


class BeatPurchase(models.Model):
    BEAT_CHOICES = [
        ('SADE', 'SADE - Afro - 100K'),
        ('Hold me', 'Hold me - Afro - 100K'),
        ('Settings', 'Settings - Private School - 150K'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    beat = models.CharField(max_length=50, choices=BEAT_CHOICES)
    proof_of_payment = models.ImageField(upload_to='payment_proofs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.beat}"