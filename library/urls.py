from django.urls import path
from .views import IdeaListView, IdeaDetailView, add_to_favorites, remove_from_favorites

urlpatterns = [
    path('', IdeaListView.as_view(), name='idea_list'),
    path('<int:pk>/', IdeaDetailView.as_view(), name='idea_detail'),
    path('favorite/add/<int:idea_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorite/remove/<int:idea_id>/', remove_from_favorites, name='remove_from_favorites'),
]