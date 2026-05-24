from django.urls import path
from . import views

urlpatterns = [
    path('', views.masterclass_list, name='masterclass_list'),
]