from django.views.generic import ListView

from .models import Item

class HomePageView(ListView):
    template_name = "homepage.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = Item.objects.filter().order_by("-id")[:10]
        return context


