from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

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
]
