from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView
)
from django.urls import reverse_lazy

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
]
