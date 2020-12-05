from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView, PasswordResetView,
    PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy

from .views import RegistrationView

app_name = 'accounts'

urlpatterns = [
    # Login
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    # Logout
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    # Change password
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='accounts/password_changed.html'
        ),
        name='password_change_done'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url=reverse_lazy('accounts:password_change_done')
        ),
        name='password_change'
    ),

    # Reset password
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='accounts/password_reset/'
            'password_reset.html',
            subject_template_name='accounts/password_reset/'
            'email_subject.txt',
            email_template_name='accounts/password_reset/'
            'email_message.html',
            success_url=reverse_lazy('accounts:password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset/'
            'email_sent.html',
        ),
        name='password_reset_done'
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset/'
            'password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset/'
            'password_reset_complete.html',
        ),
        name='password_reset_complete'
    ),

    # Registration
    path(
        'registration/',
        RegistrationView.as_view(),
        name='registration'
    )
]
