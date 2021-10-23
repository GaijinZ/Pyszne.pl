from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, RedirectView, FormView
from django.contrib.auth import logout, authenticate, login
from django.utils.encoding import force_text, force_bytes
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import RegisterForm, LoginForm
from .tokens import account_activation_token
from .models import User


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/sign-up.html'
    success_url = reverse_lazy('accounts:sign-in')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, 'Please Confirm your email to complete registration.')

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, 'Your account have been confirmed.')
            return redirect('/')
        else:
            messages.warning(
                request, 'The confirmation link was invalid, possibly because it has already been used.'
            )
            return redirect('/')


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/sign-in.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        last_name = form.cleaned_data.get('last_name')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, last_name=last_name, password=password)
        if user and user.is_active:
            login(self.request, user)
            return redirect(self.success_url)
        return super().form_invalid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
