from django.urls import path

from .views import HomeView, SearchView

app_name = 'yummy_site'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('food/', SearchView.as_view(), name='food'),
]
