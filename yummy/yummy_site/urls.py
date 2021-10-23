from django.urls import path

from .views import HomeView

app_name = 'yummy_site'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
