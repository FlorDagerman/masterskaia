from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm
from .models import User
from masterclasses.models import Booking
from library.models import Favorite

class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user).select_related('masterclass')
    favorites = Favorite.objects.filter(user=request.user).select_related('idea')
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {
        'bookings': bookings,
        'favorites': favorites,
        'form': form
    })

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
    return redirect(reverse('profile') + '#bookings')