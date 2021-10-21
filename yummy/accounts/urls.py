from django.urls import path

from .views import RegisterView, ActivateAccount, LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('sign-out-redirect/', LogoutView.as_view(), name='sign-out-redirect'),
]
