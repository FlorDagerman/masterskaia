from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Idea, Favorite
from taggit.models import Tag

class IdeaListView(ListView):
    model = Idea
    paginate_by = 12
    template_name = 'library/idea_list.html'

    def get_queryset(self):
        qs = super().get_queryset().filter(is_published=True)
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__name__in=[tag])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context

class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'library/idea_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idea = self.get_object()
        similar = Idea.objects.filter(tags__in=idea.tags.all(), is_published=True).exclude(pk=idea.pk).distinct()[:5]
        context['similar_ideas'] = similar
        return context

@login_required
def add_to_favorites(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    Favorite.objects.get_or_create(user=request.user, idea=idea)
    return redirect('idea_detail', pk=idea_id)

@login_required
def remove_from_favorites(request, idea_id):
    Favorite.objects.filter(user=request.user, idea_id=idea_id).delete()
    return redirect(reverse('profile') + '#favorites')