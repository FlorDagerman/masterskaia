from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MasterClass, Booking

class MasterClassListView(ListView):
    model = MasterClass
    paginate_by = 10
    template_name = 'masterclasses/list.html'

    def get_queryset(self):
        qs = super().get_queryset().filter(is_active=True)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category__slug=cat)
        return qs

class MasterClassDetailView(DetailView):
    model = MasterClass
    template_name = 'masterclasses/detail.html'

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = []
    template_name = 'masterclasses/booking_form.html'

    def post(self, request, pk):
        masterclass = get_object_or_404(MasterClass, pk=pk)
        if masterclass.available_seats <= 0:
            return redirect('masterclass_detail', pk=pk)
        booking = Booking.objects.create(
            user=request.user,
            masterclass=masterclass,
            status='pending'
        )
        return redirect('profile')