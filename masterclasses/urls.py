from django.urls import path
from .views import MasterClassListView, MasterClassDetailView, BookingCreateView

urlpatterns = [
    path('', MasterClassListView.as_view(), name='masterclass_list'),
    path('<int:pk>/', MasterClassDetailView.as_view(), name='masterclass_detail'),
    path('book/<int:pk>/', BookingCreateView.as_view(), name='book_masterclass'),
]