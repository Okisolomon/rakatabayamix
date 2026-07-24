from django.shortcuts import render, redirect
from .forms import StudioBookingForm, BeatPurchaseForm

def home(request):
    booking_form = StudioBookingForm()
    beat_form = BeatPurchaseForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'booking':
            booking_form = StudioBookingForm(request.POST, request.FILES)
            if booking_form.is_valid():
                booking_form.save()
                return redirect('success')

        if form_type == 'beat':
            beat_form = BeatPurchaseForm(request.POST, request.FILES)
            if beat_form.is_valid():
                beat_form.save()
                return redirect('success')

    return render(request, 'studio/home.html', {
        'booking_form': booking_form,
        'beat_form': beat_form,
    })


def success(request):
    return render(request, 'studio/success.html')