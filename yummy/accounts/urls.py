from django.urls import path

from .views import RegisterView, ActivateAccount

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]
