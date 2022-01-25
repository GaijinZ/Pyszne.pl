from django.views.generic import TemplateView, ListView

from restaurants.models import Restaurant


class HomeView(TemplateView):
    template_name = 'yummy/home.html'


class SearchView(ListView):
    template_name = 'yummy/food.html'
    model = Restaurant
    context_object_name = 'available_restaurants'

    def get_queryset(self):
        available_restaurants = Restaurant.objects.all().select_related('address')\
            .filter(address__postcode=self.request.GET.get('postcode'))
        return available_restaurants
