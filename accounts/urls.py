from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("accounts/login/",views.userLogin, name='login'),
    path("accounts/logout/",views.userLogOut, name = 'logout')
]

