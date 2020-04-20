from django.views import generic
from django.utils import timezone

from .models import Person


class AboutView(generic.DetailView):
    model = Person
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
