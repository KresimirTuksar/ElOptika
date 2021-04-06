from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("accounts/login/",auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("accounts/logout/",views.userLogOut, name = 'logout')
]

